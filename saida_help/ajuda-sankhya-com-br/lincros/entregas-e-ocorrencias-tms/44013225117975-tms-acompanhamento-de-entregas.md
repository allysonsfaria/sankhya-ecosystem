---
id: "44013225117975"
titulo: "[TMS] - Acompanhamento de Entregas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013225117975--TMS-Acompanhamento-de-Entregas"
trilha: "Lincros > TMS > Entregas e Ocorrências - TMS"
atualizado_em: "2026-10-05T19:50:33Z"
rotulos: ["sync_hc", "lincros", "lincros_13432849", "sync_hash_767c7db4cb2b"]
---

# [TMS] - Acompanhamento de Entregas

## 1. Problema Relatado pelo Cliente

O cliente deseja **acompanhar o status de entrega das NF-es** diretamente no sistema Lincros, visualizando o percurso da nota fiscal desde sua emissão até a finalização da entrega.

A funcionalidade de **Acompanhamento de Entregas** permite esse acompanhamento por meio de uma **régua de ocorrências** que mostra visualmente o progresso da entrega, e também possibilita **lançamento manual ou em lote de ocorrências**, além da **importação de  ocorrências via planilha**.
Este artigo explica as regras de negócio encontradas na tela de acompanhamento de entregas e explica como realizar o lançamento manual, em lote, ou via planilha através da tela de acompanhamento de entregas.

---

## 2. Passo a Passo para Resolver o Problema

## Pré-requisitos

- Ter **Prazos de Entrega** cadastrados. Apenas caso queira acompanhar previsão de entrega dos transportadores nos documentos listados.
- Ter **Ocorrências** cadastradas.
- São apresentados nesta tela pré-notas e notas fiscais que possuem um ou mais dos seguintes pré-conhecimentos: "Normal, Redespacho, Devolução, Reentrega e Veículo adicional".
- Para que o conhecimento de veiculo adicional seja visualizado no acompanhamento de entregas se faz necessário ativar o parâmetro de empresa visualizarReguaDeRastreioVeiculoAdicional.

---

## Acessar a Tela de Acompanhamento de Entregas

1. Acesse o caminho:
   **Menu: Entregas e Ocorrências > Acompanhamento de Entregas**
2. A tela exibirá por padrão todas as NF-es com status **"Em Transporte"**.

   - Para visualizar outros status, utilize o filtro na coluna **"Situação"**.

---

## Visualizar Detalhes da Entrega

1. Clique na seta ao lado da NF-e para expandir as informações.
2. A régua de ocorrências será exibida:

   - **Preenchimento roxo:** eventos já realizados.
   - **Preenchimento branco:** eventos previstos.

     ![Imagem 1: Preenchimento branco: eventos previstos.](https://ajuda.sankhya.com.br/hc/article_attachments/44013225326999)

O sistema calcula a previsão de entrega com base nos dados cadastrados no **menu de Prazos de Entrega**, que levam em consideração a origem, destino, dias úteis de transporte e cadastro de feriados.

---

## Lançar Ocorrência Individual

1. Para lançar uma ocorrência individual:

   - Acesse a **aba detalhes**da nota fiscal correspondente.
   - Clique em **"Lançar Ocorrência"**.
   - Preencha os campos obrigatórios:

     - **Data/Hora**
     - **Ocorrência** (pesquisável via lupa)
     - **Pré-conhecimento**
   - Após preenchimento, clique em **"Incluir"**.

⚠️ Apenas ocorrências previamente cadastradas para exibição na régua serão mostradas nela. As demais aparecerão na parte inferior da página.

---

## Lançar Ocorrências em Lote

1. Selecione as NF-es  ou pré-notas fiscais desejadas. Somente podem ser selecionados documentos de um tipo por vez. Existem algumas regras para lançamento do lote, onde, somente devem ser selecionados pré-notas OU notas e no caso das pré-notas, sempre deve possuir um conhecimento do tipo NORMAL, REDESPACHO, VEÍCULO ADICIONAL, REENTREGA ou DEVOLUÇÃO. Se o documento tiver mais de um pré-conhecimento, será vinculado sempre no conhecimento NORMAL.
2. Clique em **"Ocorrências em Lote"** e preencha a janela com as informações necessárias.

---

## Importar Ocorrências por Planilha

1. Clique na seta lateral e selecione a opção de **importar modelo não preenchido (.xlsx)**.
2. Preencha a planilha com os campos:

   - **Código da ocorrência**
   - **Data da ocorrência**
3. Após preencher, faça o upload da planilha.
4. Se não houver erros, as ocorrências serão lançadas corretamente.

---

## 3. Considerações Importantes

1. A régua de ocorrências é customizável, mas apenas exibe as ocorrências configuradas previamente para esse fim.
2. O prazo de entrega é influenciado por localidade e dias úteis, definidos no cadastro de **Prazos de Entrega**.
3. Ocorrências podem ser lançadas manualmente, em lote ou importadas via planilha, integração correios, upload de arquivo EDI OCORREN, integração do produto TRACKING LINCROS, Webservice.
4. A tela de Acompanhamento também permite **exportações em diversos formatos** para análises e registros.

Algumas das regras do acompanhamento de entregas:

**Quando uma NF assumirá o status transportada:**

Sempre que a NFe tiver uma ocorrência de baixa de entrega vinculada a cada um de seus pré-conhecimentos dos tipos: Normal, Redespacho, Veículo Adicional, Reentrega e Devolução, assumirá o status de transportada.
Há alguns parâmetros que excluem alguns tipos de conhecimento ou a obrigatoriedade da ocorrência.

**Quando um Pré-conhecimento assumirá o status transportado:**

Sempre que todas as NFes vinculadas no pré-conhecimento tiverem uma ocorrência de baixa de entrega vinculada, assumirá o status de transportado.
Há alguns parâmetros que excluem alguns tipos de conhecimento ou a obrigatoriedade da ocorrência.

**Quando uma NF assumirá o status finalizada:**

Sempre que a NFe tiver uma ocorrência de baixa de finalizar transporte vinculada, indiferente do número de pré-conhecimentos, ela assumirá o status finalizada. 

**Quando um Pré-conhecimento assumirá o status finalizado:**

Sempre que todas as NFes vinculadas no pré-conhecimento tiverem uma ocorrência de finalizar transporte vinculada, assumirá o status de finalizado.

**Caso a nota fiscal possua mais de um pré-conhecimento data de previsão e data de coleta:**
A data de coleta será exibida sempre a que está informada no conhecimento normal.

Previsão de entrega que será exibida no resumo da nota fiscal, será do último pré-conhecimento criado (conhecimento de maior OID). Há alguns parâmetros que excluem alguns tipos de conhecimento.

![Imagem 2: Sempre que todas as NFes vinculadas no pré-conhecimento tiverem uma ocorrência de finalizar transporte vinculada,…](https://ajuda.sankhya.com.br/hc/article_attachments/44013188228759)

**Explicando a regra:**

A nota possuí dois pré-conhecimentos atrelados, sendo o normal com o oid 10914139998 e o conhecimento de redespacho com oid 10916697672. Com o de redespacho possuí maior numeração, a previsão de entrega  será apresentado no resumo da nota fiscal. Como não há informação, a nota fiscal ficará sem a previsão.

**Campo atraso:**O campo atraso é a soma dos conhecimentos (Normal, Redespacho, Veiculo adicional, Reentrega e Devolução). Há alguns parâmetros que excluem alguns tipos de conhecimento.
