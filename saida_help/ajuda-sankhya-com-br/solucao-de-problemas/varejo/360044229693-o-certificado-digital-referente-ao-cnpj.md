---
id: "360044229693"
titulo: "O certificado digital referente ao CNPJ: 'X' expirou, para que seja possível realizar a operação, importe um certificado válido através da tela Console NF-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044229693-O-certificado-digital-referente-ao-CNPJ-X-expirou-para-que-seja-poss%C3%ADvel-realizar-a-opera%C3%A7%C3%A3o-importe-um-certificado-v%C3%A1lido-atrav%C3%A9s-da-tela-Console-NF-e"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-07-22T15:59:41Z"
rotulos: ["Configuração", "Fast Service", "NF-e", "SEFAZ", "Certificado digital expirado", "Atualize no Console NF-e", "Teste a comunicação do serviço", "Certificado Digital"]
---

# O certificado digital referente ao CNPJ: 'X' expirou, para que seja possível realizar a operação, importe um certificado válido através da tela Console NF-e

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16199986914199) MENSAGEM:**

O certificado digital referente ao CNPJ: 'X' expirou, para que seja possível realizar a operação, importe um certificado válido através da tela Console NF-e.

[erro: handshare=true]

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16200015795607) SITUAÇÃO:**

Mensagem apresentada ao realizar emissão de CF-e e/ou NFC-e no Fast Service.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16200015797143) SOLUÇÃO:**

Adquira certificado digital atualizado, no formato .pfx, modelo A1 e efetue a troca conforme abaixo:

**![Imagem 4: Identifique a máquina/IP, na qual o SANNFE utilizado pelo Fast encontra-se instalado:](https://ajuda.sankhya.com.br/hc/article_attachments/16199986920855) Identifique a máquina/IP, na qual o SANNFE utilizado pelo Fast encontra-se instalado:**

- Acesse o Fast Service pelo Usuário SUP;
- Na Tela Utilitários » DBEEXPLORER;
- Digite a consulta: **SELECT \* FROM TSIPAR WHERE CHAVE = 'IPSERVNFE';**
- Clique no botão **"Executar"**, ao lado direito da tela;
- Na linha retornada, dê um duplo clique no conteúdo do campo **"Texto"**;
- Copie o IP apresentado, exemplo: 192.168.1.215.

**![Imagem 5: Acesso ao 'Console NFE'](https://ajuda.sankhya.com.br/hc/article_attachments/16200015801623) Acesso ao 'Console NFE'**

- Através desse IP, abra um Navegador e digite: ' IP:9090/NFE.html';
- No nosso exemplo: 192.168.1.215:9090/NFE.html;
- Será solicitado usuário/senha, por padrão insira admin/admin;
- Concluído o acesso você estará no CONSOLE NF-e, basta então seguir com os procedimentos abaixo.

**![Imagem 6: Atualização do certificado](https://ajuda.sankhya.com.br/hc/article_attachments/16200015805207) Atualização do certificado**

- Verifique qual dos certificados está expirado e clique sobre este registro;
- Clique em **"Remover registro"**, depois em **"Sim"**;
- Para inserir o novo:  Clique em **"Inserir registro"**;
- Procure o certificado no diretório do computador;
- Informe CNPJ, Estado e Senha (repassada pelo fornecedor do certificado);
- Salvar registro.

**![Imagem 7: Testar a comunicação do serviço](https://ajuda.sankhya.com.br/hc/article_attachments/16200015806615) Testar a comunicação do serviço**

- Acesse a aba **Status Serviço**;
- Selecione o CNPJ que acabou de fornecer no novo certificado;
- Marque as Opções: "**Produção"**, "**4.0"** e "**SEFAZ"**;
- Clique **"Testar"**;
- Se retornado **"serviço em operação"**, a troca do seu certificado foi executada com sucesso, retorne suas emissões no Fast Service.
- Se retornado algum status diferente, entre em contato com o Service Desk Sankhya para análises.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16199986928151) CAUSA:**

Ao realizar emissão de CF-e e/ou NFC-e no Fast Service, na qual o certificado digital referente CNPJ da empresa emissora tenha expirado, será retornada a mensagem
