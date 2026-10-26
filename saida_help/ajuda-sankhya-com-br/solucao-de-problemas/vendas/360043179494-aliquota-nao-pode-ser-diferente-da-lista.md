---
id: "360043179494"
titulo: "Alíquota não pode ser diferente da lista de serviço"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043179494-Al%C3%ADquota-n%C3%A3o-pode-ser-diferente-da-lista-de-servi%C3%A7o"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:02:38Z"
rotulos: ["Configuração", "Alíquota de ISS", "Cidades", "Impostos", "Prefeituras", "NFS-e", "Verificar cadastro serviço", "Ajustar conforme prefeitura", "Alíquota ISS incorreta"]
---

# Alíquota não pode ser diferente da lista de serviço

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16148149832343) MENSAGEM:**

Alíquota não pode ser diferente da lista de serviço.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16148149839127) SITUAÇÃO:**

Ao tentar transmitir uma NFS-e, ocorre a seguinte mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16148173464471) SOLUÇÃO:**

![Imagem 4: Acesse: tela "Serviços" ( Caminho de acesso: Configurações » Cadastros » Produtos » Serviço ).](https://ajuda.sankhya.com.br/hc/article_attachments/16148149846423) Acesse: tela **"Serviços"** (Caminho de acesso: Configurações » Cadastros » Produtos » Serviço).

![Imagem 5: Para os 'serviços' inseridos na NFS-e rejeitada, acesse a aba Alíquota de ISS e verifique o " Percentual de ISS"…](https://ajuda.sankhya.com.br/hc/article_attachments/16148173470615) Para os 'serviços' inseridos na NFS-e rejeitada, acesse a aba **Alíquota de ISS**  e verifique o "**Percentual de ISS"** cadastrado para a cidade do parceiro destinatário dos respectivos serviços:

![Imagem 6: Para os 'serviços' inseridos na NFS-e rejeitada, acesse a aba Alíquota de ISS e verifique o " Percentual de ISS"…](https://ajuda.sankhya.com.br/hc/article_attachments/12611769814039)

![Imagem 7: De acordo com o percentual de ISS acima, verifique junto a Prefeitura e/ou Contador, se esse está de acordo com o…](https://ajuda.sankhya.com.br/hc/article_attachments/16148149852567) De acordo com o percentual de ISS acima, verifique junto a Prefeitura e/ou Contador, se esse está de acordo com o esperado.

![Imagem 8: Caso o percentual esteja incorreto, realize os devidos ajustes e realize uma nova emissão da NFS-e.](https://ajuda.sankhya.com.br/hc/article_attachments/16148173476887) Caso o percentual esteja incorreto, realize os devidos ajustes e realize uma nova emissão da NFS-e.

![Imagem 9: Caso o percentual esteja correto , verifique se a respectiva Prefeitura se enquadra na necessidade de envio do ISS com…](https://ajuda.sankhya.com.br/hc/article_attachments/16148149866775) Caso o percentual **esteja correto**, verifique se a respectiva Prefeitura se enquadra na necessidade de envio do ISS com alíquota em percentual. Em caso positivo, inserir o **"Código IBGE"** no parâmetro abaixo:

- Tela **"[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)"** (Configurações » Avançado » Preferências);
- Chave **"MUNALIQPERCNFSE"** - Cód.IBGE municípios c/ alíquota NFSe em percentual;

![Imagem 10: Após ajustes, gere um novo lote da nota de serviço.](https://ajuda.sankhya.com.br/hc/article_attachments/16148173486487) Após ajustes, gere um novo lote da nota de serviço.

**![Imagem 11: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16148173489303) CAUSA:**

Ocorre quando a respectiva prefeitura não aceita o percentual de alíquota de ISS, fazendo com o que o sistema divida o % (percentual) por 100.
