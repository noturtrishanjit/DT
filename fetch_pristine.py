import urllib.request, urllib.parse, json, subprocess

genuine_queries = [
    {"id": "track_kesariya", "title": "Kesariya", "artist": "Pritam, Arijit Singh & Amitabh Bhattacharya", "query": "Kesariya Pritam Brahmastra", "genre": "Bollywood / Romantic", "year": "2022"},
    {"id": "track_tum_hi_ho", "title": "Tum Hi Ho", "artist": "Arijit Singh & Mithoon", "query": "Tum Hi Ho Aashiqui 2 Arijit Singh", "genre": "Bollywood / Soul", "year": "2013"},
    {"id": "track_apna_bana_le", "title": "Apna Bana Le", "artist": "Arijit Singh & Sachin-Jigar", "query": "Apna Bana Le Bhediya Arijit Singh", "genre": "Bollywood / Romantic", "year": "2022"},
    {"id": "track_channa_mereya", "title": "Channa Mereya", "artist": "Arijit Singh & Pritam", "query": "Channa Mereya Ae Dil Hai Mushkil", "genre": "Bollywood / Heartbreak", "year": "2016"},
    {"id": "track_satranga", "title": "Satranga", "artist": "Arijit Singh & Shreyas Puranik", "query": "Satranga Animal Arijit Singh", "genre": "Bollywood / Emotion", "year": "2023"},
    {"id": "track_pehle_bhi_main", "title": "Pehle Bhi Main", "artist": "Vishal Mishra & Raj Shekhar", "query": "Pehle Bhi Main Animal Vishal Mishra", "genre": "Bollywood / Melodic", "year": "2023"},
    {"id": "track_lover", "title": "Lover", "artist": "Diljit Dosanjh", "query": "Lover Diljit Dosanjh MoonChild Era", "genre": "Punjabi Pop", "year": "2021"},
    {"id": "track_born_to_shine", "title": "Born to Shine", "artist": "Diljit Dosanjh", "query": "Born to Shine Diljit Dosanjh", "genre": "Punjabi / Swagger", "year": "2020"},
    {"id": "track_goat", "title": "G.O.A.T.", "artist": "Diljit Dosanjh", "query": "G.O.A.T. Diljit Dosanjh", "genre": "Punjabi Hip-Hop", "year": "2020"},
    {"id": "track_295", "title": "295", "artist": "Sidhu Moose Wala", "query": "295 Sidhu Moose Wala Moosetape", "genre": "Punjabi Rap", "year": "2021"},
    {"id": "track_so_high", "title": "So High", "artist": "Sidhu Moose Wala & BYG BYRD", "query": "So High Sidhu Moose Wala", "genre": "Punjabi / Trap", "year": "2017"},
    {"id": "track_last_ride", "title": "The Last Ride", "artist": "Sidhu Moose Wala & Wazir Patar", "query": "The Last Ride Sidhu Moose Wala", "genre": "Punjabi Hip-Hop", "year": "2022"},
    {"id": "track_tauba_tauba", "title": "Tauba Tauba", "artist": "Karan Aujla", "query": "Tauba Tauba Karan Aujla Bad Newz", "genre": "Bollywood / Punjabi", "year": "2024"},
    {"id": "track_winning_speech", "title": "Winning Speech", "artist": "Karan Aujla & MXRCI", "query": "Winning Speech Karan Aujla", "genre": "Punjabi / Rap", "year": "2024"},
    {"id": "track_excuses", "title": "Excuses", "artist": "AP Dhillon & Gurinder Gill", "query": "Excuses AP Dhillon", "genre": "Punjabi Pop", "year": "2020"},
    {"id": "track_brown_munde", "title": "Brown Munde", "artist": "AP Dhillon, Gurinder Gill & Shinda Kahlon", "query": "Brown Munde AP Dhillon", "genre": "Punjabi Hip-Hop", "year": "2020"},
    {"id": "track_insane", "title": "Insane", "artist": "AP Dhillon & Gurinder Gill", "query": "Insane AP Dhillon", "genre": "Punjabi / Drill", "year": "2021"}
]

java_code = """
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
"""
with open("/tmp/DecryptPristine.java", "w") as f:
    f.write(java_code)
subprocess.run(["javac", "/tmp/DecryptPristine.java"], check=True)

proc = subprocess.Popen(["java", "-cp", "/tmp", "DecryptPristine"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

out = []
for item in genuine_queries:
    q = urllib.parse.quote(item["query"])
    url = f"https://www.jiosaavn.com/api.php?__call=search.getResults&_format=json&_marker=0&api_version=4&ctx=web6dot0&n=5&p=1&q={q}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode())
            results = data.get("results", [])
            for r in results:
                t = r.get("title", "")
                tl = t.lower()
                if any(bad in tl for bad in ["karaoke", "instrumental", "nightcore", "sped", "slowed", "cover", "remake", "tribute", "zzang"]):
                    continue
                enc = r.get("more_info", {}).get("encrypted_media_url", "")
                if not enc: continue
                dur = int(r.get("more_info", {}).get("duration", "180"))
                art = r.get("image", "").replace("150x150", "500x500").replace("50x50", "500x500")
                alb = r.get("more_info", {}).get("album", "Single").replace("&quot;", "\"").replace("&#039;", "'").replace("&amp;", "&")
                proc.stdin.write(enc + "\n")
                proc.stdin.flush()
                media_url = proc.stdout.readline().strip()
                out.append({
                    "id": item["id"],
                    "title": item["title"],
                    "artist": item["artist"],
                    "album": alb,
                    "durationSeconds": dur,
                    "artworkUrl": art,
                    "audioUrl": media_url,
                    "genre": item["genre"],
                    "releaseDate": item["year"]
                })
                print("OK:", item["title"], "->", dur, "sec", "| Album:", alb)
                break
    except Exception as e:
        print("ERR:", item["title"], e)

proc.stdin.close()
with open("/tmp/pristine_catalog.json", "w") as f:
    json.dump(out, f, indent=2)
print("TOTAL PRISTINE TRACKS:", len(out))
