---
id: "360043863794"
titulo: "Como realizar a troca de certificado digital - MGE Mitra/ G1?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043863794-Como-realizar-a-troca-de-certificado-digital-MGE-Mitra-G1"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T15:58:30Z"
rotulos: ["DUVIDANF", "Configuração", "Fast Service", "NF-e", "SEFAZ", "Troca certificado digital - MGE Mitra/ G1", "Providencie novo certificado A1 (.pfx) e senha", "Atualize certificado no Navegador Sankhya", "Configure IP em Preferências", "Certificado Digital"]
---

# Como realizar a troca de certificado digital - MGE Mitra/ G1?

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17129605732503) SITUAÇÃO:**

Existem situações em que o certificado digital da empresa é renovado ou foi expirado seu prazo de uso. Por esse motivo se faz necessário trocá-lo no sistema.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17129605737879) SOLUÇÃO:**

![Imagem 3: Providencie o novo certificado (modelo A1 e extensão .pfx) e a senha, junto ao seu fornecedor de certificados, antes de…](https://ajuda.sankhya.com.br/hc/article_attachments/17129605740823) Providencie o novo certificado (modelo A1 e extensão .pfx) e a senha, junto ao seu fornecedor de certificados, antes de iniciar os procedimentos de troca;

![Imagem 4: No sistema acesse: Avançado >> Preferências >> Todas as Preferências;](https://ajuda.sankhya.com.br/hc/article_attachments/17129576569879) No sistema acesse: Avançado >> Preferências >> Todas as Preferências;

![Imagem 5: Digite a chave: " IPSERVNFE" ;](https://ajuda.sankhya.com.br/hc/article_attachments/17129605746455) Digite a chave: **"IPSERVNFE"**;

![Imagem 6: Copie o IP apresentado nessa chave;](https://ajuda.sankhya.com.br/hc/article_attachments/17129605750295) Copie o IP apresentado nessa chave;

![Imagem 7: Dentro do N avegador Sankhya , acesse o endereço: XXXXXXXX:9090/NFE.html e substitua o 'XXXXXXXX' pelo IP copiado no…](https://ajuda.sankhya.com.br/hc/article_attachments/17129605753367) Dentro do [**Navegador Sankhya**](http://downloads.sankhya.com.br/), acesse o endereço: XXXXXXXX:9090/NFE.html e substitua o 'XXXXXXXX' pelo IP copiado no parâmetro mencionado acima. Será solicitado usuário/senha, por padrão insira admin/admin

- Registre o endereço dentro do [**Navegador Sankhya**](http://downloads.sankhya.com.br/) em: Configurações >> registrar novo servidor.

- Concluído o acesso, o usuário estará no **CONSOLE NF-e.** Então, siga com os procedimentos abaixo:

![Imagem 8: Concluído o acesso, o usuário estará no CONSOLE NF-e. Então, siga com os procedimentos abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/4404089524247)

![Imagem 9: Verifique qual dos certificados está expirado e clique sobre este registro;](https://ajuda.sankhya.com.br/hc/article_attachments/17129605757207) Verifique qual dos certificados está expirado e clique sobre este registro;

![Imagem 10: Clique em " Remover registro ", depois em "Sim";](https://ajuda.sankhya.com.br/hc/article_attachments/17129605765143) Clique em "**Remover registro**", depois em **"Sim";**

#### **(1)** Inserir novo certificado:

![Imagem 11: Clique em "Inserir registro" ;](https://ajuda.sankhya.com.br/hc/article_attachments/17129605740823) Clique em **"Inserir registro"**;

![Imagem 12: Procure o novo certificado no diretório do computador;](https://ajuda.sankhya.com.br/hc/article_attachments/17129576569879) Procure o novo certificado no diretório do computador;

![Imagem 13: Informe CNPJ, Estado e Senha (repassada pelo fornecedor do certificado);](https://ajuda.sankhya.com.br/hc/article_attachments/17129605746455) Informe CNPJ, Estado e Senha (repassada pelo fornecedor do certificado);

![Imagem 14: Salve o registro.](https://ajuda.sankhya.com.br/hc/article_attachments/17129605750295) Salve o registro.

#### **(1)** Para testar a comunicação do serviço:

![Imagem 15: Acesse a aba "Status Serviço";](https://ajuda.sankhya.com.br/hc/article_attachments/17129605740823) Acesse a aba **"Status Serviço";**

![Imagem 16: Selecione o CNPJ que acabou de fornecer o novo certificado;](https://ajuda.sankhya.com.br/hc/article_attachments/17129576569879) Selecione o CNPJ que acabou de fornecer o novo certificado;

![Imagem 17: Marque as Opções : " Produção" (se emissão for em produção), Versão NF-e ( 4.0 ) e Ambiente de envio ( SEFAZ );](https://ajuda.sankhya.com.br/hc/article_attachments/17129605746455) Marque as Opções : **"Produção"** (se emissão for em produção), Versão NF-e [**4.0**] e Ambiente de envio [**SEFAZ**];

![Imagem 18: Clique "Testar";](https://ajuda.sankhya.com.br/hc/article_attachments/17129605750295) Clique **"Testar";**

![Imagem 19: Clique "Testar";](https://ajuda.sankhya.com.br/hc/article_attachments/4404095370775)

- Caso retorne **"Serviço em Operação"**: a troca foi efetuada com sucesso.
- Diante de algum status diferente desse, faça uma busca pela nossa Central de Ajuda e, caso necessário, acione o Service Desk.

**![Imagem 20: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17129605769111) OBSERVAÇÃO:**

Para clientes que emitem NFC-e pelo**Fast Service**, insira o novo certificado pelo Console do servidor local onde está instalado o SanNFe, **utilizando também o Navegador Sankhya.**

**(1)**Acesse o artigo e veja como baixar o Navegador Sankhya: **[Navegador Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599474-Navegador-Sankhya)**
