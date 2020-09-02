package logic.connection;

import java.util.HashMap;
import java.util.Map;
import java.util.Properties;
import javax.activation.DataHandler;
import javax.activation.DataSource;
import javax.activation.FileDataSource;
import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.Multipart;
import javax.mail.PasswordAuthentication;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeBodyPart;
import javax.mail.internet.MimeMessage;
import javax.mail.internet.MimeMultipart;


/*
 * Libreria para el manejo de envío de correos electronicos
 */
/**
 *
 * @author Brian Botina
 */
public class Email {

    private String sourceMail;
    private String password;
    private String destinationMail;
    private Map<String, String> attachFiles;
    private final Properties PROPERTIES;
    private Session session;

    public Email() {
        PROPERTIES = new Properties();
        attachFiles = new HashMap();
    }

    public void setProperties(Map<String, String> properties) {
        properties.entrySet().forEach((entry) -> {
            String key = entry.getKey();
            String value = entry.getValue();
            PROPERTIES.put(key, value);
        });
    }

    public void setAuthentication(String isTrue) {
        PROPERTIES.put("mail.smtp.auth", isTrue);
    }

    public void enableTTLS(String isTrue) {
        PROPERTIES.put("mail.smtp.starttls.enable", isTrue);
    }

    public void setHost(String host) {
        PROPERTIES.put("mail.smtp.host", host);
    }

    public void setPort(String port) {
        PROPERTIES.put("mail.smtp.port", "587");
    }

    public void enableSSL(String isTrue) {
        PROPERTIES.put("mail.smtp.EnableSSL.enable", isTrue);
    }

    public void setSourceMail(String sourceMail) {
        this.sourceMail = sourceMail;
    }

    public void setDestinationMail(String destinationMail) {
        this.destinationMail = destinationMail;
    }

    public void addAttachFile(String attachName, String pathFile) {
        if (attachFiles == null) {
            attachFiles = new HashMap();
        }
        this.attachFiles.put(attachName, pathFile);

    }

    public void setPassword(String password) {
        this.password = password;
    }

    public boolean SendEmail(String subject, String bodyText) throws MessagingException {
        session = Session.getInstance(PROPERTIES,
                new javax.mail.Authenticator() {
            @Override
            protected PasswordAuthentication getPasswordAuthentication() {
                return new PasswordAuthentication(sourceMail, password);
            }
        });

        Message message = new MimeMessage(session);
        message.setFrom(new InternetAddress(sourceMail));
        message.setRecipients(Message.RecipientType.TO, InternetAddress.parse(destinationMail));
        message.setSubject(subject);
        MimeBodyPart messageBodyPart = new MimeBodyPart();
        Multipart multipart = new MimeMultipart();
        messageBodyPart.setText(bodyText);
        multipart.addBodyPart(messageBodyPart);
        for (Map.Entry<String, String> entry : attachFiles.entrySet()) {
            String attachName = entry.getKey();
            String filePath = entry.getValue();
            messageBodyPart = new MimeBodyPart();
            DataSource source = new FileDataSource(filePath);
            messageBodyPart.setDataHandler(new DataHandler(source));
            messageBodyPart.setFileName(attachName);
            multipart.addBodyPart(messageBodyPart);
        }
        message.setContent(multipart);
        Transport.send(message);

        return true;
    }
}
