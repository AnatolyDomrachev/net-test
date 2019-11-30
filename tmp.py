

*Для чего нужна система  DNS?
# +DNS позволяет по доменному имени узла узнать его IP адрес.
' - DNS позволяет по доменному имени узла узнать его MAC адрес.'
- DNS позволяет по доменному имени узла узнать его шлюз.
- DNS позволяет по IP узнать его маску подсети.

*По какому протоколу и на каких портах работает DNS сервер?
+DNS серверы работают на 53 порту UDP для обработки запросов и на 53 порту TCP для передачи файлов зон.
--------- - DNS серверы работают на 54 порту UDP для обработки запросов и на 53 порту TCP для передачи файлов зон.
- DNS серверы работают на 53 порту HTTP для обработки запросов и на 53 порту TCP для передачи файлов зон.
-DNS серверы работают на 54 порту IP для обработки запросов и на 53 порту ETHERNET для передачи файлов зон.

*Что такое домен, поддомен, зона, делегирование?
+Домен DNS – часть имён, заканчивающихся одинаково. 
Поддомен – домен, входящий в состав другого домена.  
Зона – домен без своих поддоменов.  
Делегирование – передача полномочий по управлению доменом другому лицу. 
- Домен DNS – часть имён, начинающихся одинаково. Например, 
Поддомен – домен, входящий в состав другого домена.  
Зона – домен без своих поддоменов. 
Делегирование – передача полномочий по управлению доменом другому лицу. 
- Домен DNS – часть имён, начинающихся одинаково. 
Поддомен – часть имён, заканчивающихся одинаково.
Зона – домен без своих поддоменов.
 Делегирование – передача полномочий по управлению доменом другому лицу. 
-Домен DNS – часть имён, заканчивающихся одинаково. 
Поддомен – домен, входящий в состав другого домена.  
Зона – домен с 1 и более поддоменов.  
Делегирование – передача полномочий по управлению доменом другому лицу. 

*Какие существуют типы DNS записей и для чего они используются?
+A – преобразует имя в ИП адрес ; NS - Связывает имя домена с именем сервера имён, используется для делегирования ; CHAME - Связывает дополнительные имена с записью A; MX - Связывает домен с адресом почтового сервера ; SOA - Указывает параметры зоны
- A – преобразует имя в МАС адрес ; NS - Связывает имя домена с именем поддомена, используется для делегирования ; CHAME - Связывает дополнительные имена с записью A; MX - Связывает домен с адресом почтового сервера ; SOA - Указывает параметры зоны
- A – преобразует имя в IP адрес ; NS - Связывает имя домена с именем поддомена, используется для делегирования ; CHAME - Связывает домен с адресом почтового сервера A; MX - Связывает дополнительные имена с записью ; SOA - Указывает параметры зоны
-A – преобразует имя в ИП адрес ; NS - Связывает домен с адресом почтового сервера, используется для делегирования ; CHAME - Связывает дополнительные имена с записью A; MX - Связывает имя домена с именем сервера имён ; SOA - Указывает параметры поддомена

*Приведите пример делегирования домена в лабораторной работе.
+nngasu.ru       IN       NS      ns.nngasu.ru     (ru)
- nngasu.ru       IN       MX      mx.nngasu.ru     (ru)
- nngasu.ru       ON       NS      ns.nngasu.ru     (ru)
- nngasu.ru       ON       MX     mx.nngasu.ru     (ru)

*Чем отличаются рекурсивный и не рекурсивный DNS серверы, каким должен быть сервер провайдера?
+нерекурсивным  - может выдавать только записи из своих зон.
рекурсивный  -  может начать перенаправлять запросы другим серверам. Сервер провайдера должен быть рекурсивным для своих клиентов.
-нерекурсивным  - может выдавать только записи из своих поддоменов.
рекурсивный  -  может начать перенаправлять запросы другим серверам. Сервер провайдера должен быть рекурсивным для своих клиентов.
- нерекурсивным  - может выдавать только записи из своих зон.
рекурсивный  -  может начать перенаправлять запросы другим серверам. Сервер провайдера должен быть нерекурсивным для своих клиентов.
- нерекурсивным  - может выдавать только записи из своих зон.
рекурсивный  -  не может выдавать записи. Сервер провайдера должен быть рекурсивным для своих клиентов.

*Как сделать так, чтобы те, кто получил от вас DNS ответ, не хранили его долго в своём кэше?
+Изменить время в SOA.
-Изменить время в SAO.
-Изменить статус в SOA.
-Изменить статус в SAO.

*Опишите процесс поиска IP адреса в системе DNS, начиная с отправки запроса компьютером.
+DNS имеет иерархическую древовидную структуру, подобную структуре файловой системы. В корне системы находится домен «точка», который представлен 9-ю серверами имён a.root-servers.net, b.root-servers.net и др. Эти серверы содержат одинаковую информацию, они делегирует полномочия своим поддоменам географическим и тематическим (ru, com, net и тд.).

