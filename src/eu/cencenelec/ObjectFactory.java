
package eu.cencenelec;

import javax.xml.namespace.QName;
import jakarta.xml.bind.JAXBElement;
import jakarta.xml.bind.annotation.XmlElementDecl;
import jakarta.xml.bind.annotation.XmlRegistry;


/**
 * This object contains factory methods for each 
 * Java content interface and Java element interface 
 * generated in the eu.cencenelec package. 
 * <p>An ObjectFactory allows you to programatically 
 * construct new instances of the Java representation 
 * for XML content. The Java representation of XML 
 * content can consist of schema derived interfaces 
 * and classes representing the binding of schema 
 * type definitions, element declarations and model 
 * groups.  Factory methods for each of these are 
 * provided in this class.
 * 
 */
@XmlRegistry
public class ObjectFactory {

    private static final QName _Books_QNAME = new QName("", "books");

    /**
     * Create a new ObjectFactory that can be used to create new instances of schema derived classes for package: eu.cencenelec
     * 
     */
    public ObjectFactory() {
    }

    /**
     * Create an instance of {@link BooksType }
     * 
     * @return
     *     the new instance of {@link BooksType }
     */
    public BooksType createBooksType() {
        return new BooksType();
    }

    /**
     * Create an instance of {@link TitleType }
     * 
     * @return
     *     the new instance of {@link TitleType }
     */
    public TitleType createTitleType() {
        return new TitleType();
    }

    /**
     * Create an instance of {@link BookType }
     * 
     * @return
     *     the new instance of {@link BookType }
     */
    public BookType createBookType() {
        return new BookType();
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link BooksType }{@code >}
     * 
     * @param value
     *     Java instance representing xml element's value.
     * @return
     *     the new instance of {@link JAXBElement }{@code <}{@link BooksType }{@code >}
     */
    @XmlElementDecl(namespace = "", name = "books")
    public JAXBElement<BooksType> createBooks(BooksType value) {
        return new JAXBElement<>(_Books_QNAME, BooksType.class, null, value);
    }

}
