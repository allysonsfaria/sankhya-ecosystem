---
id: "26405446974487"
titulo: "Ao clicar em esqueci a senha no SankhyaW o erro é apresentado 'Consulte o manual do Sankhya W para obter informações de como utilizar esta operação'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26405446974487-Ao-clicar-em-esqueci-a-senha-no-SankhyaW-o-erro-%C3%A9-apresentado-Consulte-o-manual-do-Sankhya-W-para-obter-informa%C3%A7%C3%B5es-de-como-utilizar-esta-opera%C3%A7%C3%A3o"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T14:42:17Z"
rotulos: ["Configuração", "Segurança", "Preferências", "Passos para resolver", "Razão do erro", "Detalhe do erro", "'Consulte o manual do Sankhya W para obter informações de como utilizar esta operação'", "clicar em esqueci a senha no SankhyaW o erro é apresentado", "Erro", "SankhyaW"]
---

# Ao clicar em esqueci a senha no SankhyaW o erro é apresentado 'Consulte o manual do Sankhya W para obter informações de como utilizar esta operação'

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/26405453057175) **MENSAGEM:**

Ao clicar em esqueci a senha no SankhyaW o erro é apresentado 'Consulte o manual do Sankhya W para obter informações de como utilizar esta operação'.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26405446966935)SOLUÇÃO:**

**Siga as orientações abaixo para solucionar a questão:**

![Imagem 3: Entre no sistema Sankhya W com um usuário que tenha permissões para realizar ajustes de configuração na tela…](https://ajuda.sankhya.com.br/hc/article_attachments/27968576012567) Entre no sistema Sankhya W com um usuário que tenha permissões  para realizar ajustes de configuração na tela **"Preferências"** (Configurações » Avançado » Preferências);

![Imagem 4: Localize o Parâmetro "ENDACESSEXTWGE - Endereço para acesso externo ao WGE" e atualize o valor deste parâmetro para…](https://ajuda.sankhya.com.br/hc/article_attachments/27968576015767) Localize o Parâmetro **"ENDACESSEXTWGE - Endereço para acesso externo ao WGE"** e atualize o valor deste parâmetro para incluir o endereço de acesso externo correto. Este endereço deve ser a URL que os usuários usarão para acessar a funcionalidade de recuperação de senha;

![Imagem 5: Após atualizar o parâmetro, certifique-se de salvar as alterações. Retorne ao login e selecione a opção "Esqueci minha…](https://ajuda.sankhya.com.br/hc/article_attachments/27968549491991) Após atualizar o parâmetro, certifique-se de salvar as alterações. Retorne ao login e selecione a opção **"Esqueci minha senha"**, assim receberá uma mensagem no e-mail (anteriormente configurado no cadastro do usuário) com a opção de redefinir sua senha;

![Imagem 6: Siga as instruções do e-mail para redefinir a senha e faça um teste de login para confirmar que o problema foi…](https://ajuda.sankhya.com.br/hc/article_attachments/27968549494807) Siga as instruções do e-mail para redefinir a senha e faça um teste de login para confirmar que o problema foi resolvido.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26405453062807)CAUSA:**

O erro ocorre porque o parâmetro **ENDACESSEXTWGE** não está configurado corretamente. Esse parâmetro é responsável por definir o endereço de acesso externo necessário para que a funcionalidade de recuperação de senha funcione corretamente.
