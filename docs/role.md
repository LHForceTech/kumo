# Role

A seção **`role`** define o comportamento do container da aplicação:

   - **`nome_role`**: Define uma função ou papel que pode representar um grupo de configurações específicas para um ou mais hosts.
   - **`hosts`**: Lista de IPs ou nomes de hosts onde o serviço será executado. Neste exemplo, `192.168.1.1`.
   - **`labels`**: Define rótulos para Traefik, configurando rotas, pontos de entrada e TLS, entre outras coisas.
   - **`options`**: Especifica limites de recursos como memória e CPUs.
   - **`env`**: Variáveis de ambiente específicas para o papel.

Podem existir mais de uma **role**, como por exemplo, a aplicação e um job.