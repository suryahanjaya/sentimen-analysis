# =============================================================================
# Scraping Google Play Store Reviews
# =============================================================================
# Script ini melakukan scraping ulasan dari Google Play Store
# menggunakan library google-play-scraper untuk mengumpulkan
# dataset analisis sentimen dengan 3 kelas: Negatif, Netral, Positif
# =============================================================================

import pandas as pd
from google_play_scraper import reviews, Sort
import time
import os

# Daftar aplikasi populer Indonesia untuk di-scraping
APPS = {
    'com.gojek.app': 'Gojek',
    'com.grabtaxi.passenger': 'Grab',
    'com.tokopedia.tkpd': 'Tokopedia',
    'com.shopee.id': 'Shopee',
    'id.dana': 'Dana',
    'com.traveloka.android': 'Traveloka',
    'com.lazada.android': 'Lazada',
    'com.tiket.gits': 'Tiket.com',
    'id.flip': 'Flip',
    'com.whatsapp': 'WhatsApp',
    'com.instagram.android': 'Instagram',
    'com.spotify.music': 'Spotify',
    'com.twitter.android': 'Twitter',
    'com.linkedin.android': 'LinkedIn',
    'id.bmri.livin': 'Livin Mandiri',
    'com.bca.mybca': 'myBCA',
    'src.com.bni': 'BNI Mobile',
    'com.telkomsel.telkomselcm': 'MyTelkomsel',
    'com.indosat.myim3': 'myIM3',
}

# Jumlah review per aplikasi
REVIEWS_PER_APP = 1500

def scrape_reviews(app_id, app_name, count=REVIEWS_PER_APP):
    """Scraping ulasan dari satu aplikasi di Google Play Store.
    
    Args:
        app_id (str): ID aplikasi di Play Store
        app_name (str): Nama aplikasi untuk identifikasi
        count (int): Jumlah ulasan yang ingin diambil
        
    Returns:
        list: Daftar ulasan yang berhasil diambil
    """
    print(f"\n{'='*60}")
    print(f"Scraping: {app_name} ({app_id})")
    print(f"{'='*60}")
    
    all_reviews = []
    batch_size = 200
    continuation_token = None
    
    while len(all_reviews) < count:
        try:
            result, continuation_token = reviews(
                app_id,
                lang='id',           # Bahasa Indonesia
                country='id',        # Indonesia
                sort=Sort.NEWEST,    # Urutkan berdasarkan terbaru
                count=batch_size,
                continuation_token=continuation_token
            )
            
            if not result:
                print(f"  Tidak ada lagi ulasan untuk {app_name}")
                break
            
            for review in result:
                review_data = {
                    'app_name': app_name,
                    'username': review.get('userName', ''),
                    'score': review.get('score', 0),
                    'content': review.get('content', ''),
                    'thumbsUpCount': review.get('thumbsUpCount', 0),
                    'reviewCreatedVersion': review.get('reviewCreatedVersion', ''),
                    'at': str(review.get('at', '')),
                    'replyContent': review.get('replyContent', ''),
                }
                all_reviews.append(review_data)
            
            print(f"  Berhasil mengambil {len(all_reviews)} ulasan...")
            time.sleep(1)  # Delay untuk menghindari rate limiting
            
            if continuation_token is None:
                break
            
        except Exception as e:
            print(f"  Error saat scraping {app_name}: {str(e)}")
            time.sleep(2)
            break
    
    return all_reviews[:count]


def label_sentiment(score):
    """Melabeli sentimen berdasarkan rating bintang.
    
    Args:
        score (int): Rating bintang (1-5)
        
    Returns:
        str: Label sentimen (negatif/netral/positif)
    """
    if score <= 2:
        return 'negatif'
    elif score == 3:
        return 'netral'
    else:
        return 'positif'


def main():
    """Fungsi utama untuk menjalankan proses scraping."""
    print("=" * 60)
    print("SCRAPING GOOGLE PLAY STORE REVIEWS")
    print("Analisis Sentimen - Dicoding Submission")
    print("=" * 60)
    
    all_data = []
    
    for app_id, app_name in APPS.items():
        reviews_data = scrape_reviews(app_id, app_name)
        all_data.extend(reviews_data)
        print(f"  Total data terkumpul: {len(all_data)}")
        time.sleep(2)  # Delay antar aplikasi
    
    # Konversi ke DataFrame
    df = pd.DataFrame(all_data)
    
    # Hapus ulasan kosong
    df = df[df['content'].str.strip().astype(bool)]
    
    # Hapus duplikat
    df = df.drop_duplicates(subset=['content'])
    
    # Tambahkan label sentimen
    df['sentiment'] = df['score'].apply(label_sentiment)
    
    # Reset index
    df = df.reset_index(drop=True)
    
    # Tampilkan statistik
    print("\n" + "=" * 60)
    print("HASIL SCRAPING")
    print("=" * 60)
    print(f"Total ulasan: {len(df)}")
    print(f"\nDistribusi sentimen:")
    print(df['sentiment'].value_counts())
    print(f"\nDistribusi per aplikasi:")
    print(df['app_name'].value_counts())
    
    # Simpan dataset
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dataset.csv')
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"\nDataset berhasil disimpan di: {output_path}")
    print(f"Jumlah total sampel: {len(df)}")
    
    return df


if __name__ == '__main__':
    main()
