import io.searchbox.client.JestClientFactory;
import io.searchbox.client.JestResult;
import io.searchbox.client.config.HttpClientConfig;
import io.searchbox.client.http.JestHttpClient;
import io.searchbox.core.Get;
import io.searchbox.core.Search;
import io.searchbox.core.search.sort.Sort;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * User: qin.qq
 * Date: 2017/5/12
 * Time: 下午9:53
 */
public class SearchTest {

    private JestHttpClient client;
    private String indexName = "qmht-event";

    @Before
    public void before(){

        List<String> servList = new ArrayList<String>();
        servList.add("http://localhost:9200");
        servList.add("http://localhost:9200");

        JestClientFactory factory = new JestClientFactory();
        factory.setHttpClientConfig(
                new HttpClientConfig.Builder(servList).multiThreaded(true).build()
        );

        client = (JestHttpClient) factory.getObject();
        System.out.println(client.getAsyncClient());

    }


    @Test
    public void testGetById() {
        String id = "3";
        Get get = new Get.Builder(indexName, id).build();
        try {
            JestResult rs = client.execute(get);
            System.out.println(rs.getJsonString());
            System.out.println(rs.getSourceAsObjectList(Product.class));
            System.out.println(rs.getSourceAsObject(Product.class));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }



    @Test
    public void testSearchByTag() {
        String tag1 = "TEST卫衣";
        String tag2 = "卫衣";

        String query = "{\n" +
                "  \"query\": {\n" +
                "    \"bool\": {\n" +
                "      \"must\": [\n" +
                "        {\n" +
                "          \"term\": {\n" +
                "            \"tag\": \"" + tag1 + "\"\n" +
                "          }\n" +
                "        }\n" +
                "      ],\n" +
                "      \"must_not\": [],\n" +
                "      \"should\": []\n" +
                "    }\n" +
                "  },\n" +
                "  \"from\": 0,\n" +
                "  \"size\": 10\n" +
                "}"  ;
        ;
        try {
            JestResult rs = client.execute(
                    new Search.Builder(query).addSort(new Sort("id", Sort.Sorting.DESC)
            ).build());
            System.out.println(rs.getJsonString());
            System.out.println(rs.getSourceAsObjectList(Product.class));
            System.out.println(rs.getSourceAsObject(Product.class));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }




    @After
    public void after(){
        client.shutdownClient();
    }


}
