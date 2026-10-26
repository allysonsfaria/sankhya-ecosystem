---
id: "35056533976983"
titulo: "Houve erro no processo de envio de código de liberação! Foram enviados um total de 0 e-mail(s)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35056533976983-Houve-erro-no-processo-de-envio-de-c%C3%B3digo-de-libera%C3%A7%C3%A3o-Foram-enviados-um-total-de-0-e-mail-s"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:26:05Z"
rotulos: ["Configuração", "Contas", "SMTP", "Contas SMTP", "Erro", "autorização", "autorização de customizalção", "codigo liberação", "código de liberação", "Houve erro no processo de envio de código de liberação! Foram enviados um total de 0 e-mail(s)", "Artigo atualizado KCS"]
---

# Houve erro no processo de envio de código de liberação! Foram enviados um total de 0 e-mail(s)

### Código de Autorização de Customização Não Chega no E-mail

**MENSAGEM**

Houve erro no processo de envio do código de liberação! Foram enviados um total de 0 e-mail(s) e houve a seguinte mensagem de erro: Verifique a configuração de "Conta Padrão" do cadastro "Contas SMTP". Envio de e-mail exige autenticação de usuário, verifique configuração de usuário.

**SITUAÇÃO**

Na rotina **"Autorização de Customizações"**, o sistema gera um código de liberação que deve ser enviado por e-mail ao autorizador. Se a conta SMTP definida como padrão estiver ausente ou mal configurada, o processo não envia nenhum e-mail (0 e-mail(s)) e exibe a mensagem de erro. Em alguns casos, mesmo quando o sistema não apresenta erro, o **código não é recebido pelo destinatário**, impedindo a continuidade do processo de liberação de customizações.

**SOLUÇÃO**

Para resolver o problema de não recebimento do código de autorização, siga os passos abaixo:

**(1)**  Acesse a tela **"Contas SMTP"** (Configurações Avançado Envio de Mensagens Contas SMTP) e verifique se existe uma **conta configurada como "Conta Padrão"**.

**(2)**  Certifique-se de que os campos de **autenticação de usuário** (usuário e senha) estão **preenchidos corretamente** na conta SMTP configurada. No formulário de **"Contas SMTP"**, existe a opção **"Conta padrão"**. Apenas uma conta pode estar marcada como padrão.

**(3)**  Se não houver conta padrão, selecione uma das contas SMTP existentes e marque-a como padrão. Caso contrário, realize um **teste de envio** pela tela **"Contas SMTP"** para validar se o serviço de e-mail está funcional. Verifique autorizações, autenticação, servidor, porta, tipo de conexão (SSL/TLS), usuário/senha ou OAuth, conforme configurado.

**(4)**  Caso o teste de envio seja bem-sucedido, mas o código de autorização ainda não chegue, **verifique junto ao provedor de e-mail** se há bloqueios, filtros de spam ou regras de segurança que possam estar impedindo o recebimento de mensagens do domínio Sankhya.

**(5)**  Solicite ao provedor de e-mail a **liberação do domínio** ou endereço de envio utilizado pelo sistema para garantir o recebimento das mensagens.

**(6)**  Verifique a **caixa de spam ou lixo eletrônico** do destinatário, pois o e-mail pode ter sido direcionado para essas pastas.

**CAUSA**

A conta SMTP designada como **"Conta Padrão"** no cadastro de **"Contas SMTP"** não está definida. Ou a conta padrão existe, mas possui configuração incorreta ou está inoperante (dados inválidos, autenticação não concluída ou servidor SMTP inacessível). Consequentemente, o sistema não consegue identificar qual conta deve usar para o envio, ou usa uma conta padrão inválida, resultando em falha no envio. O problema pode ocorrer por **duas causas principais**:

**1. Falta de configuração da conta SMTP:** quando não há uma **"Conta Padrão"** configurada ou quando os dados de autenticação (usuário e senha) estão incorretos ou ausentes, o sistema não consegue enviar o e-mail, resultando na mensagem de erro.

**2. Bloqueio pelo provedor de e-mail do destinatário:** mesmo com o sistema enviando o e-mail corretamente (sem erros nos logs), o **provedor de e-mail do cliente pode estar bloqueando** a mensagem devido a políticas de segurança, filtros antispam ou regras de firewall que impedem o recebimento de mensagens do domínio Sankhya.
