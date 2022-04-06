# Noverde
API de análise de crédito para a Noverde. São utilizadas as seguintes tecnologias:

* **Python** como linguagem base
* **Django** para framework web
* **Django Rest Framework** para framework REST
* **PostgreSQL** para banco de dados
* **PgAdmin** para interface de administração do banco de dados
* **Celery** como gerenciador de fila de tarefas
* **RabitMQ** como broker de mensagens do Celery
* **Docker** para fazer o deploy da stack localmente

Para colocar o serviço no ar, é recomendado possuir o Git e o Docker instalado na máquina local (localhost).
Com esses requisitos, pode-se começar clonando este repositório, através dos seguintes comandos:

    $ git clone 
    $ cd noverde

Após isso, levante o servidor através do comando:

    $ sudo docker-compose -f stack.yml up

Após isso, a API já está disponível no endereço `http://localhost:81`.

O gerenciador do banco de dados pgadmin pode ser acessado pelo endereço `http://localhost:82`.  O usuário para acesso
ao pgadmin é `pgadmin@teste.com` e a senha é `pgadmin_pass`.

Adicione um novo server com as seguintes informações:

* Host name/adress: db
* Port: 5432
* Maintenance database: noverde
* Username: noverde_user
* Password: noverde_pass

Enjoy!
