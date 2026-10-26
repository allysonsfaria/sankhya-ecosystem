---
id: "360044110094"
titulo: "O prazo de validade de uso do certificado importado expirou"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110094-O-prazo-de-validade-de-uso-do-certificado-importado-expirou"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:53:53Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "SEFAZ", "Certificado Digital Expirado no SanNFE", "Certificado Digital", "Erro"]
---

# O prazo de validade de uso do certificado importado expirou

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16618356658711) MENSAGEM:**

O prazo de validade de uso do certificado importado expirou.
**Observação**: esta data refere-se ao prazo permitido para utilização do certificado no SanNFE e não a data de expiração do certificado digital.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16618356663191) SOLUÇÃO:**

Para correção, siga os passos abaixo:

Tenha a seu acesso o **arquivo .pfx do certificado digital atual** da empresa e sua respectiva **senha**.

![Imagem 3: Acesse a tela "Console NFe" (Caminho de acesso: Comercial » Configuração);](https://ajuda.sankhya.com.br/hc/article_attachments/16618356666007) Acesse  a tela **"Console NFe"** (Caminho de acesso: Comercial » Configuração);

![Imagem 4: Selecione o certificado referente ao CNPJ emissor o qual está ocorrendo o problema;](https://ajuda.sankhya.com.br/hc/article_attachments/16618356669591) Selecione o certificado referente ao CNPJ emissor o qual está ocorrendo o problema;

![Imagem 5: Clique em "Remover registro", depois em "Sim".](https://ajuda.sankhya.com.br/hc/article_attachments/16618356672663) Clique em "Remover registro", depois em "Sim".

**(1)** Para inserir o novo:

![Imagem 6: Clique em "Inserir registro";](https://ajuda.sankhya.com.br/hc/article_attachments/16618347522071) Clique em "Inserir registro";

![Imagem 7: Procure o certificado no diretório do computador;](https://ajuda.sankhya.com.br/hc/article_attachments/16618356680471) Procure o certificado no diretório do computador;

![Imagem 8: Informe CNPJ, Estado e Senha (repassada pelo fornecedor do certificado);](https://ajuda.sankhya.com.br/hc/article_attachments/16618347526807) Informe CNPJ, Estado e Senha (repassada pelo fornecedor do certificado);

![Imagem 9: Salve o registro.](https://ajuda.sankhya.com.br/hc/article_attachments/16618347528087) Salve o registro.

**(1)** Depois de reinstalar o certificado é necessário testar a comunicação do serviço:

![Imagem 10: Acesse a aba Status Serviço;](https://ajuda.sankhya.com.br/hc/article_attachments/16618347534743) Acesse a aba Status Serviço;

![Imagem 11: Selecione o CNPJ que acabou de fornecer no novo certificado;](https://ajuda.sankhya.com.br/hc/article_attachments/16618347536279) Selecione o CNPJ que acabou de fornecer no novo certificado;

![Imagem 12: Marque as Opções > Produção, 4.0 e SEFAZ;](https://ajuda.sankhya.com.br/hc/article_attachments/16618356694167)  Marque as Opções > Produção, 4.0 e SEFAZ;

![Imagem 13: Clique em "Testar".](https://ajuda.sankhya.com.br/hc/article_attachments/16618356697495)  Clique em "Testar".

- Caso retorne **"Serviço em Operação"** é porque a troca foi efetuada com sucesso;
- Se retornar algum outro status, entre em contato com o Service Desk Sankhya Jiva;
- Acesse o Console NF-e, exclua o certificado anteriormente atualizado e insira novamente, via opção 'Inserir Registro' com o certificado Raiz;
- Salve o novo certificado.

**![Imagem 14: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16618356699799) CAUSA:**

Ocorre pela expiração da data de utilização do certificado digital no SanNFE.

Geralmente quando se utiliza a opção de Exportar via aba: Administração, botão 'Importação/Exportação' e é inserido uma data menor que a data de validade do certificado, quando se exporta o certificado.
