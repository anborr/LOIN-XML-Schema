package eu.cencenelec;

import java.io.*;
import jakarta.xml.bind.*;

public class Generator {
    public static void main(String[] args) {
        Generator gen = new Generator();
        try {
            gen.marshal();
        } catch (JAXBException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public void marshal() throws JAXBException, IOException {
        ObjectFactory factory = new ObjectFactory();

        BookType myBook = new BookType();
        myBook.setId("ID_bc30bde4-f590-11ed-b67e-0242ac120002");
        myBook.setPrice("24.55");
        TitleType myTitle = new TitleType();
        myTitle.setValue("Building Information Modeling");
        myTitle.setLang("en");
        myBook.setTitle(myTitle);
        myBook.setYear("2018");

        BooksType booklist = new BooksType();
        booklist.getBook().add(myBook);;

        JAXBElement<BooksType> element = factory.createBooks(booklist);

        JAXBContext context = JAXBContext.newInstance(BooksType.class);
        Marshaller mar= context.createMarshaller();
        mar.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, Boolean.TRUE);
        mar.marshal(element, new File("./src/xml/Bookstore-Example/booklist-generated.xml"));
    }
}




