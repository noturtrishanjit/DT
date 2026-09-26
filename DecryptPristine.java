
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;
import java.util.Scanner;

public class DecryptPristine {
    public static void main(String[] args) throws Exception {
        SecretKeySpec key = new SecretKeySpec("38346591".getBytes(), "DES");
        Cipher cipher = Cipher.getInstance("DES/ECB/PKCS5Padding");
        cipher.init(Cipher.DECRYPT_MODE, key);
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextLine()) {
            String enc = sc.nextLine().trim();
            if (enc.isEmpty()) continue;
            try {
                byte[] decoded = Base64.getDecoder().decode(enc);
                byte[] decrypted = cipher.doFinal(decoded);
                String url = new String(decrypted);
                url = url.replace("_96.mp4", "_160.mp4");
                System.out.println(url);
            } catch (Exception e) {
                System.out.println("ERROR");
            }
        }
    }
}
