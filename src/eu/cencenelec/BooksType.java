
package eu.cencenelec;

import java.util.ArrayList;
import java.util.List;
import jakarta.xml.bind.annotation.XmlAccessType;
import jakarta.xml.bind.annotation.*;


/**
 * <p>Java-Klasse für booksType complex type.
 * 
 * <p>Das folgende Schemafragment gibt den erwarteten Content an, der in dieser Klasse enthalten ist.
 * 
 * <pre>{@code
 * <complexType name="booksType">
 *   <complexContent>
 *     <restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *       <sequence>
 *         <element name="book" type="{}bookType" maxOccurs="unbounded" minOccurs="0"/>
 *       </sequence>
 *     </restriction>
 *   </complexContent>
 * </complexType>
 * }</pre>
 * 
 * 
 */

@XmlRootElement(name = "books",namespace = "https://www.cencenelec.eu/bookstore")
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "booksType", propOrder = {
    "book"
})
public class BooksType {

    @XmlElement(namespace = "https://www.cencenelec.eu/bookstore")
    protected List<BookType> book;

    /**
     * Gets the value of the book property.
     * 
     * <p>
     * This accessor method returns a reference to the live list,
     * not a snapshot. Therefore any modification you make to the
     * returned list will be present inside the Jakarta XML Binding object.
     * This is why there is not a {@code set} method for the book property.
     * 
     * <p>
     * For example, to add a new item, do as follows:
     * <pre>
     *    getBook().add(newItem);
     * </pre>
     * 
     * 
     * <p>
     * Objects of the following type(s) are allowed in the list
     * {@link BookType }
     * 
     * 
     * @return
     *     The value of the book property.
     */
    public List<BookType> getBook() {
        if (book == null) {
            book = new ArrayList<>();
        }
        return this.book;
    }

}
