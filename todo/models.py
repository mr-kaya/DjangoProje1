from django.db import models

#Database oluşturma alanıdır.

#Aşağıda database'in özellikleri belirtilmiştir.
#Database tanımlanırken Id tanımlamaya gerek yoktur, django kendisi bir Id atar ve bu Id'ye primary key özelliği verir.

class Todo(models.Model):
    title = models.CharField(max_length = 50, verbose_name = "Başlık")
    completed = models.BooleanField(verbose_name = "Durum")

    #todo ifadelerinin başlıklarını adimin panelde yazmak için kullanılır.
    def __str__(self):
        return self.title


#Bunları yazdıktan sonra, bu bilgileri admin panelinde göstermek için admin.py'de işlemleri yap.