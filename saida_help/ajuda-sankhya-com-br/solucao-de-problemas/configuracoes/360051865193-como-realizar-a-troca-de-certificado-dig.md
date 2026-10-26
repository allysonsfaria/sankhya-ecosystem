---
id: "360051865193"
titulo: "Como realizar a troca de certificado digital para o Fast Service"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360051865193-Como-realizar-a-troca-de-certificado-digital-para-o-Fast-Service"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:30:11Z"
rotulos: ["Configuração", "Fast Service", "NF-e", "SEFAZ", "Troca de Certificado Digital no Fast Service", "Certificado Digital"]
---

# Como realizar a troca de certificado digital para o Fast Service

![Imagem 1: Providencie o novo certificado ( modelo A1 e extensão .pfx ) e a senha, junto ao seu fornecedor de certificados antes…](https://ajuda.sankhya.com.br/hc/article_attachments/15936313738263) Providencie o novo certificado (**modelo A1 e extensão .pfx**) e a senha, junto ao seu fornecedor de certificados antes de iniciar os procedimentos de troca.

![Imagem 2: Execute os passos abaixo para descobrir o IP do servidor de NFE:](https://ajuda.sankhya.com.br/hc/article_attachments/15936335288983) Execute os passos abaixo para descobrir o IP do servidor de NFE:

- Acesse o Fast Service através do usuário SUP;
- Selecione a  opção 'Utilitários > DbeExplorer' ;
- Copie a expressão: **SELECT \* FROM TSIPAR WHERE CHAVE ='IPSERVNFE'** e execute essa consulta.

![Imagem 3: Copie o IP apresentado na consulta;](https://ajuda.sankhya.com.br/hc/article_attachments/15936313741335) Copie o IP apresentado na consulta;

![Imagem 4: Em qualquer navegador, acesse o endereço: XXXXXXXX:9090/NFE.html (substitua o 'XXXXXXXX' pelo IP copiado no parâmetro…](https://ajuda.sankhya.com.br/hc/article_attachments/15936335291799) Em qualquer navegador, acesse o endereço: **XXXXXXXX:9090/NFE.html** (substitua o 'XXXXXXXX' pelo IP copiado no parâmetro mencionado acima);

Será solicitado usuário/senha, por padrão inserir:

- Usuário: admin
- Senha: admim

Concluído o acesso você estará no **CONSOLE NF-e**, basta então seguir com os procedimentos abaixo:

![Imagem 5: Verifique qual dos certificados está expirado e clique sobre este registro:](https://ajuda.sankhya.com.br/hc/article_attachments/15936335293207) Verifique qual dos certificados está expirado e clique sobre este registro:

![Imagem 6: Verifique qual dos certificados está expirado e clique sobre este registro:](https://ajuda.sankhya.com.br/hc/article_attachments/360082181414)

![Imagem 7: Clique em " Remover registro ", depois em "Sim"](https://ajuda.sankhya.com.br/hc/article_attachments/15936335294231) Clique em "**Remover registro**", depois em "Sim"

**Inserir novo certificado:**

- Clique em "Inserir registro".
- Procure o novo certificado no diretório do computador.
- Informe CNPJ, Estado e Senha (informada pelo fornecedor do certificado).
- Salvar registro.

**Para testar a comunicação do serviço:**

- Acesse a aba 'Status Serviço'.
- Selecione o CNPJ que acabou de fornecer o novo certificado.
- Marque as Opções : **Produção**(Se emissão for em produção), Versão NF-e [**4.0**] e Ambiente de envio [**SEFAZ**].
- Clique "Testar".

![Imagem 8: Clique "Testar".](https://ajuda.sankhya.com.br/hc/article_attachments/360083302333)

- Caso retorne **"Serviço em Operação"** : A troca foi efetuada com sucesso.
- Diante status diferente desse, faça uma busca pela nossa Central de Ajuda, e caso necessário acione o Service Desk.
