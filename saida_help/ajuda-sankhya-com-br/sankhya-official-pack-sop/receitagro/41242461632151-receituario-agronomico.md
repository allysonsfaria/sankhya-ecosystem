---
id: "41242461632151"
titulo: "Receituário Agronômico"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41242461632151-Receitu%C3%A1rio-Agron%C3%B4mico"
trilha: "Sankhya Official Pack - SOP > ReceitAgro"
atualizado_em: "2026-07-22T13:26:58Z"
rotulos: ["Configuração", "Fiscal", "SEFAZ", "Agrônomos", "Receituário Agronômico", "Consulta Fitossanitária", "Alvos / Pragas", "Culturas Agrícolas", "Configuração ReceitaAgro", "Produtores Rurais", "Documentos Eletrônicos", "WebReceita"]
---

# Receituário Agronômico

O Receituário Agronômico conecta o Sankhya Om à plataforma WebReceita, emitindo o receituário agronômico automaticamente no momento do faturamento da nota fiscal. O vendedor trabalha apenas na Central de Notas — o sistema cuida do resto.

| **IMPORTANTE:** Nenhum herbicida, fungicida ou inseticida pode ser comercializado sem receituário agronômico assinado por agrônomo habilitado. Exigência da Lei 7.802/89 — o descumprimento gera multas e suspensão da licença de comercialização. |
| --- |

### Pré-requisitos

Antes de configurar o módulo no Sankhya, a empresa precisa:

**(1)**Contratar o serviço da WebReceita diretamente com o fornecedor.

**(2)** Obter as credenciais de integração (Client ID e Client Secret).

**(3)** Garantir que os agrônomos estejam habilitados na plataforma com CREA/CFTA e ARTs ativas.

| **Nota:** Sem contratação ativa da WebReceita, nenhuma importação, exportação ou emissão será possível — toda comunicação depende das credenciais da plataforma. |
| --- |

### Configuração ReceitaAgro

Na tela **''Configuração ReceitaAgro''** (Receita Agro » Cadastros » Configuração ReceitaAgro), informe a plataforma (WebReceita), cole as credenciais recebidas na contratação e marque o registro como Ativo. Essa configuração é feita uma única vez.

![Imagem 1: Na tela ''Configuração ReceitaAgro'' (Receita Agro » Cadastros » Configuração ReceitaAgro), informe a plataforma…](https://ajuda.sankhya.com.br/hc/article_attachments/41242474183831)

**OBSERVAÇÃO:** Só é necessário revisitar essa tela quando a plataforma renovar as credenciais de acesso.

### Consulta Fitossanitária

A tela **''Consulta Fitossanitária''** (Receita Agro » Cadastros » Consulta Fitossanitária) traz para dentro do Sankhya todos os defensivos registrados no MAPA. Clique em Sincronizar Produtos para importar ou atualizar a base. Cada produto exibe Nome, Registro MAPA e Plataforma.

![Imagem 2: A tela ''Consulta Fitossanitária'' (Receita Agro » Cadastros » Consulta Fitossanitária) traz para dentro do Sankhya…](https://ajuda.sankhya.com.br/hc/article_attachments/41242461597591)

#### Relação Alvo x Cultura

Na aba **''Relação Alvo x Cultura''**, clique em **''Sincronizar Alvos x Culturas''** para importar as combinações permitidas de produto × cultura × alvo (dose mínima/máxima, volume de calda e número de aplicações).

![Imagem 3: Na aba ''Relação Alvo x Cultura'' , clique em ''Sincronizar Alvos x Culturas'' para importar as combinações permitidas…](https://ajuda.sankhya.com.br/hc/article_attachments/41242474188567)

| **Nota:** Essa base é o que valida as prescrições na hora da venda — mantenha-a sempre atualizada. |
| --- |

#### Vínculo Produto ERP

Na aba **''Vínculo Produto ERP''**, vincule o defensivo importado ao produto correspondente no estoque do Sankhya. Sem esse vínculo, o item não é elegível ao receituário.

![Imagem 4: Na aba ''Vínculo Produto ERP'' , vincule o defensivo importado ao produto correspondente no estoque do Sankhya. Sem…](https://ajuda.sankhya.com.br/hc/article_attachments/41242461599895)

**OBSERVAÇÃO:** Um mesmo defensivo pode ser vinculado a vários produtos do estoque — útil para embalagens e marcas diferentes do mesmo princípio ativo.

### Alvos / Pragas

A tela **''Alvos / Pragas''** (Receita Agro » Cadastros » Alvos / Pragas) registra os alvos biológicos (pragas, doenças e plantas daninhas) importados da WebReceita. Clique em **''Sincronizar Alvos''** para atualizar a base local.

![Imagem 5: A tela ''Alvos / Pragas'' (Receita Agro » Cadastros » Alvos / Pragas) registra os alvos biológicos (pragas, doenças e…](https://ajuda.sankhya.com.br/hc/article_attachments/41242474192023)

### Culturas Agrícolas

A tela **''Culturas'**' (Receita Agro » Cadastros » Culturas) registra as culturas agrícolas (soja, milho, café...) importadas da plataforma.

Clique em **''Sincronizar Culturas''** para atualizar.

![Imagem 6: Clique em ''Sincronizar Culturas'' para atualizar.](https://ajuda.sankhya.com.br/hc/article_attachments/41242461605911)

### Tipo de Operação (TOP)

O ReceitaAgro adiciona a aba **''ReceitaAgro''** no cadastro de TOPs.

Marque a opção **''Emite Receituário''** nas TOPs de Pedido venda e Venda de defensivos.

![Imagem 7: Marque a opção ''Emite Receituário'' nas TOPs de Pedido venda e Venda de defensivos.](https://ajuda.sankhya.com.br/hc/article_attachments/41242474197399)

| **IMPORTANTE:** TOPs não marcadas seguem 100% inalteradas. O bloqueio de confirmação de nota só ocorre em documentos que usam TOPs com Emite Receituário ativo. |
| --- |

### Agrônomos

A tela **''Agrônomos''** (Receita Agro » Cadastros » Agronomos) cadastra e sincroniza os responsáveis técnicos com a WebReceita. Use **''Exportar Agrônomo''** ou **''Sincronizar Agrônomos''** para manter os dados atualizados em ambos os lados.

#### Aba CREA

Registra o número do CREA/CFTA, a ART e a quantidade de receitas autorizadas. O campo **''Receitas Emitidas''** é atualizado automaticamente a cada emissão.

![Imagem 8: Registra o número do CREA/CFTA, a ART e a quantidade de receitas autorizadas. O campo ''Receitas Emitidas'' é…](https://ajuda.sankhya.com.br/hc/article_attachments/41242461612695)

| **IMPORTANTE:** Quando a quota da ART é esgotada, o sistema bloqueia novas emissões para o agrônomo. Cadastre uma nova ART para liberar. |
| --- |

#### Aba Geral

Registra CPF/CNPJ, profissão e endereço do agrônomo — dados obrigatórios para a emissão.

![Imagem 9: Registra CPF/CNPJ, profissão e endereço do agrônomo — dados obrigatórios para a emissão.](https://ajuda.sankhya.com.br/hc/article_attachments/41242474201495)

### Produtores Rurais

A tela **''Produtores''** (Receita Agro » Cadastros » Produtores) vincula o parceiro Sankhya ao cadastro da plataforma (pelo CPF/CNPJ) e registra os dados exigidos no receituário:

- Nome da propriedade,
- Inscrição estadual,
- Município,
- Local de aplicação,
- Coordenadas GPS.

![Imagem 10: Coordenadas GPS.](https://ajuda.sankhya.com.br/hc/article_attachments/41242474202903)

**OBSERVAÇÃO:** O campo E-mail é essencial: é para ele que o sistema envia automaticamente o receituário em PDF e a NF-e ao final da venda. Use os botões Exportar Produtores ou Importar Produtores para sincronizar com a WebReceita.

### Fluxo de venda — dia a dia

Para o vendedor, o processo muda muito pouco em relação ao fluxo normal:

**(1)** Crie o pedido na **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas) com uma TOP marcada como Emite Receituário.

**(2)** Informe o Agrônomo Responsável no cabeçalho da nota.

**(3)** Adicione os itens e, para cada defensivo, preencha na aba **''ReceitaAgro do item''**:

- Cultura,
- Alvo Biológico,
- Dose,
- Nº de Aplicações,
- Volume de Calda,
- Área Tratada.

**(4)** Confirme a nota — o sistema irá validar todos os dados antes de permitir a confirmação.

**(5)** Após aprovação da NF-e pela SEFAZ, o receituário é emitido automaticamente na WebReceita e o número é gravado na nota.

**(6)** O produtor recebe o receituário em PDF e a NF-e por e-mail automaticamente.

| **IMPORTANTE:** Se qualquer dado estiver incompleto, a confirmação é bloqueada com mensagem indicando exatamente o que corrigir. Não é possível faturar defensivos sem o receituário completo. |
| --- |

| **Nota:** Se a WebReceita estiver fora do ar no momento do faturamento, a nota é gerada normalmente e o receituário fica com status Pendente para reprocessamento posterior. |
| --- |

### Pós-emissão

Após a emissão, três ações estão disponíveis diretamente na Central de Notas:

- Imprimir Receituário — busca o PDF oficial na plataforma pelo código gravado na nota.
- Cancelar Receituário — solicita cancelamento à WebReceita e atualiza o status para Cancelado.
- Auditar — todas as informações (número, data/hora, status, agrônomo) ficam gravadas na nota, dispensando acesso à plataforma.

**IMPORTANTE:** Ao cancelar o receituário, o documento perde a validade legal. Confirme a ação apenas quando necessário.
