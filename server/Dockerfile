#kullanılacak sistemi belirttim
FROM python:latest

# COPY komutu ile aynı işlemi yapar.Container içerisine internetten veya local den data kopyalamak için kullanılır.
ADD Server.py /server/Server.py

#Bu komut, imajınızın temel dizinini değiştirir.
# Burada '/server/' dizinini temel dizin olarak tanımlıyoruz.
WORKDIR /server/

#Containerın docker içinde calısacagı port adresini belirledik
EXPOSE 4444

#Belirtilen komutları image icerisinde calıstırır
CMD ["python","Server.py"]
