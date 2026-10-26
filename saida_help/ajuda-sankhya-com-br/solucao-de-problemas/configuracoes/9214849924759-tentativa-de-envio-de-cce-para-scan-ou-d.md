---
id: "9214849924759"
titulo: "Tentativa de envio de CCe para SCAN ou DPEC"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9214849924759-Tentativa-de-envio-de-CCe-para-SCAN-ou-DPEC"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:09:26Z"
rotulos: ["Configuração", "NF-e", "Portal de Vendas", "XML", "SEFAZ", "CORE_E04926", "Erro ao Enviar CCe: SEFAZ Indisponível", "Erro"]
---

# Tentativa de envio de CCe para SCAN ou DPEC

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18694140472471) MENSAGEM:**

[CORE\_E04926] Tentativa de envio de CCe para SCAN ou DPEC. A carta de correção só pode ser enviada para a Receita Federal (SEFAZ), no momento essa não se encontra em operação.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18694164162711) SITUAÇÃO:**

Ao tentar confirmar uma carta de correção no portal de vendas a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18694140479639) CAUSA:**

Poderá ocorrer por instabilidade na SEFAZ, falta de comunicação no Console NF-e ou problema especificamente para o estado de GO.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18694140482071) SOLUÇÃO:**

- Pode ocorrer por alguma instabilidade na SEFAZ;
- Quando não houver comunicação no Console NF-e, realize o teste de conexão na tela: **Console NF-e** (Caminha de acesso à tela: Comercial » Configuração » Console NFe) na aba 'Status do Serviço botão'. testar.
- ![Imagem 5: Quando não houver comunicação no Console NF-e, realize o teste de conexão na tela: Console NF-e (Caminha de acesso à…](https://ajuda.sankhya.com.br/hc/article_attachments/18694140487447)
- Se a carta de correção for para o estado de Goiás e apresentar a mensagem: 'Não é possível assinar XML a UF (GO)', siga as orientações descritas no artigo abaixo:

  [Não é possível assinar xml a uf (GO) exige a cadeia de certificado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042866074)
