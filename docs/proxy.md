# Proxy

A seção **`proxy`** define o comportamento do proxy reverso (Traefik):

   - **`name`**: Nome do proxy.
   - **`options`**: Inclui configurações de publicação de portas e volumes.
   - **`args`**: Parâmetros para configurar pontos de entrada (como HTTP e HTTPS), API e certificados.
   - **`labels`**: Define rotas e serviços dentro do Traefik, além de configurações como autenticação básica (`basicauth.users`).

### Observações:
- **Traefik**: Esse arquivo está configurando várias rotas, redirecionamento de TLS, certificação Let's Encrypt, e uma API para o dashboard do Traefik.
- **Autenticação**: Para autenticação básica (`basicauth`), foi incluído um hash de senha (`traefik_user:pass_hash`). 
