FROM python:latest
ADD Client.py /client/Client.py
# Burada '/client/' dizinini temel dizin olarak tanımlıyoruz.
WORKDIR /client/
#Çalıştırılabilir bir imaj oluşturduk.
ENTRYPOINT ["python", "Client.py"]
#burada expose vermeyeceğiz çünkü server üzerinden baglanacağız.