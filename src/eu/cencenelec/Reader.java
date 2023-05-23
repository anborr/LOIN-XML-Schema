

package eu.cencenelec;

import java.io.*;
import jakarta.xml.bind.*;
import java.util.List;

public class Reader {
    public static void main(String[] args) {
        Reader reader = new Reader();
        try {
            reader.unmarshal();
        } catch (JAXBException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public void unmarshal() throws JAXBException, IOException {
        ObjectFactory factory = new ObjectFactory();

        File xmlFile = new File("./src/xml/Bookstore-Example/booklist-generated.xml");

        JAXBContext jaxbContext;

        jaxbContext = JAXBContext.newInstance(BooksType.class);
        Unmarshaller unmarshaller = jaxbContext.createUnmarshaller();
        BooksType booksListType = (BooksType) unmarshaller.unmarshal(xmlFile);

        List<BookType> bookList = booksListType.getBook();

        for (BookType book : bookList)
        {
            System.out.println(book.getId());
        }


    }
}


