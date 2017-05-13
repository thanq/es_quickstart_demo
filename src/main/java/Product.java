import io.searchbox.annotations.JestId;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import java.util.List;


@Getter
@Setter
@ToString
public class Product {

    @JestId
    private Long id;

    private String eventId;

    private String title;

    private Integer stock;

    private Double price;

    private String hasSpec;

    private List<String>  color;

    private List<String> size;

    private List<String> tag;

    private String addTime;

    
}
