---
id: "360044612174"
titulo: "Notas Pendentes de Autorização"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612174-Notas-Pendentes-de-Autoriza%C3%A7%C3%A3o"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Documentos Fiscais Eletrônicos > Comum a todos os documentos"
atualizado_em: "2026-09-15T15:01:03Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Autorização", "NF-e", "SEFAZ", "DANFE", "IMPDANNFEBUSAUT", "LISTAUFNFEASYNC", "Notas Pendentes de Autorização", "TEREFNOTAPEAUT", "br.com.sankhya.mgecom.notas.pendentes.autorizacao", "Notas Pendentes de Autorização manual", "NFS-e", "Documentos Eletrônicos"]
---

# Notas Pendentes de Autorização

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311925718295) Módulo: Comercial > Consulta
```

---

Durante o processo de emissão de Notas Fiscais Eletrônicas, podem ocorrer casos em que a empresa gera várias Notas Fiscais Eletrônicas em um curto período de tempo; este processo pode dificultar a resposta da [SEFAZ](https://www.nfe.fazenda.gov.br/portal/principal.aspx) quanto à autorização/aprovação das notas, bem como atrasar as impressões dos DANFE's, ficando a nota com o status de Aguardando Autorização.

Esta tela tem por objetivo, trabalhar exclusivamente com notas que se encontram neste status, de modo que a cada intervalo de tempo (definição feita por parâmetro), automaticamente o sistema busca a autorização das notas junto a Secretaria de Estado da Fazenda.

![NPA1](https://ajuda.sankhya.com.br/hc/article_attachments/360061025054)

No lado superior direito da tela, temos um temporizador que é atualizado de acordo com definição feita no parâmetro **"Tempo em minutos p/ atualizar nota pend. autorização - TEREFNOTAPEAUT"**, ou seja, a cada período de tempo, é feita a tentativa de autorização de notas junto à SEFAZ. Em caso de insucesso, novas tentativas serão realizadas de acordo com o tempo definido no parâmetro; se a SEFAZ autorizar a nota, o sistema obedece à sequência de processo normal estabelecida na empresa, que geralmente é a impressão do DANFE.

**Parâmetros importantes:**

Além do parâmetro TEREFNOTAPEAUT já mencionado, é necessário atentar para outras duas parametrizações:

- **Lista de UFs com autorização de NF-e assíncrona - LISTAUFNFEASYNC:** Informe neste parâmetro a sigla da Unidade Federativa da empresa que emite a Nota Fiscal Eletrônica;
- **Imprime Danfe ao buscar autorização de NF-e? - IMPDANNFEBUSAUT:** Este parâmetro é o responsável por solicitar ou não a impressão do DANFE ao buscar a autorização das notas; para que seja feita a impressão do documento, o parâmetro deve estar ativado.

Vale reforçar que a tela Notas Pendentes de Autorização será populada apenas por documentos que foram enviados à SEFAZ, porém não foram autorizados, ou seja, a coluna **"Status NF-e"** visível na grade [Resultado da seleção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601454-Portal-de-Vendas-Atributos-da-Tela#grade-resultadodaseleo) do [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601454-Portal-de-Vendas-), está como **"Aguardando Autorização"**.

Esta tela conta também com a possibilidade de criação de Filtros personalizados para visualização das notas com base em critérios específicos, bem como, a utilização de Filtros rápidos compostos pelo campo **"Empresa"** (pode ser utilizado caso sejam emitidas notas por mais de uma empresa cadastrada no sistema) e pela marcação **"Apenas notas lançadas por mim"**, que se realizada, apresentará as notas Aguardando Autorização que foram inclusas no sistema pelo usuário logado. Além disso, o campo **"Tipo"** permite alternar a visualização das notas entre NFS-e, NF-e ou Ambos.
