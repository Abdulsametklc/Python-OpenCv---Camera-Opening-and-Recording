import cv2

#capture

cap = cv2.VideoCapture(0) #bir video yakalama nesnesi oluşturuyoruz, '0' argümanı, pcye bağlı birinci kamera ile iletişim kurulacağının belirtisi..

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width,height) #bu fonksiyonlar ile kameranın çerçeve boyutlarını hesaplayıp ekrana yazdırırsınız.

#video kaydet #cv2.VideoWriter() fonksiyonunu kullanarak bir video yazma nesnesi oluşturursunuz.
#İlk argüman, kaydedilecek video dosyasının adını belirtir.
#İkinci argüman, video codec'i belirten dört karakterden oluşan bir kodlama (örneğin, "DIVX"). 
#Üçüncü argüman, FPS (frame per second) değerini belirtir (burada 20). 
#Son argüman, çerçeve boyutlarını belirtir.
writer = cv2.VideoWriter("video_kaydi.mp4",cv2.VideoWriter_fourcc(*"DIVX"),20,(width,height))

while True: 
    #Bu döngü, kameradan sürekli olarak çerçeveler okur ve bunları ekranda gösterir. 
    #cap.read() fonksiyonu, kameradan bir çerçeve okur ve ret değişkeni True ise okuma başarılıdır. 
    #Okunan çerçeve, frame değişkenine atanır. 
    #Ardından, çerçeveyi görüntülemek için cv2.imshow() kullanılır ve writer.write(frame) ile çerçeve video dosyasına kaydedilir.
    
    ret, frame = cap.read()
    cv2.imshow("Video",frame)
    
    #♠save
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release() #kamera kaynağı serbest bırakılır.
writer.release() #video yazma nesnesi serbest bırakılır.
cv2.destroyAllWindows() #tüm pencereler kapatılır.


