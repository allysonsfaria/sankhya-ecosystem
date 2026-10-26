---
id: "44010954273687"
titulo: "[Routing] - Gerar rotas de First-Mile e Last-Mile em uma única sessão de roteirização"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010954273687--Routing-Gerar-rotas-de-First-Mile-e-Last-Mile-em-uma-%C3%BAnica-sess%C3%A3o-de-roteiriza%C3%A7%C3%A3o"
trilha: "Lincros > Roteirizador"
atualizado_em: "2026-10-05T18:51:41Z"
rotulos: ["sync_hc", "lincros", "lincros_13439423", "sync_hash_594845fb5cd4"]
---

# [Routing] - Gerar rotas de First-Mile e Last-Mile em uma única sessão de roteirização

**Objetivo:** Instruir os cadastros necessários para roteirizar as duas etapas do transporte em uma única sessão, permitindo o controle completo do fluxo logístico desde a origem até o cliente final.

## Considerações:

Para operações logísticas que precisam controlar todo o fluxo de roteirização — seja a primeira perna (First-Mile), seja a segunda perna (Last-Mile) — o Routing permite planejar as duas etapas do processo em uma única sessão, integrando corretamente os embarques no TMS.

## Terminologia

- **Primeira Perna (First-Mile):** rota inicial que leva os pedidos de uma fábrica, matriz ou ponto equivalente até um centro de distribuição.
- **Segunda Perna (Last-Mile):** rota final que leva os pedidos de um centro de distribuição até o cliente final.
- **Depósito:** ponto de origem das mercadorias — pode ser matriz, fábrica ou equivalente. É de onde saem os pedidos da primeira perna.
- **Ponto de Apoio:** centro de distribuição intermediário. É onde chegam os pedidos do depósito e de onde partem para o cliente final.

## Pré-requisitos e configurações

1. Entre em contato com o suporte da Lincros pelo **Intercom** e solicite a ativação do parâmetro que habilita a roteirização das duas etapas na mesma sessão.
2. Certifique-se de ter o **depósito principal** e os respectivos **pontos de apoio** cadastrados no sistema. O ponto de apoio exige: nome, depósito de referência e coordenadas (ponto de interesse).
3. Para os veículos que realizam a **segunda perna**, no cadastro do veículo, ative a flag **"Sair do depósito/ponto de apoio no início das entregas/coletas"** e informe o ponto de apoio que o veículo atende.

   ![Imagem 1: Para os veículos que realizam a segunda perna , no cadastro do veículo, ative a flag "Sair do depósito/ponto de apoio…](https://ajuda.sankhya.com.br/hc/article_attachments/44010983654679)
4. Vincule os veículos ao respectivo setor como **preferenciais**. Esse vínculo é utilizado quando a roteirização é realizada de forma automática.

   ![Imagem 2: Vincule os veículos ao respectivo setor como preferenciais . Esse vínculo é utilizado quando a roteirização é realizada…](https://ajuda.sankhya.com.br/hc/article_attachments/44010965729431)
5. No cadastro do **ponto de apoio**, selecione o depósito referente à transferência e informe o **tempo de descarga** da rota de transferência.

O tempo de descarga garante que o veículo da primeira perna chegue ao ponto de apoio e descarregue a mercadoria em tempo hábil para que o veículo da segunda perna inicie sua jornada no horário previsto.

**Exemplo:** se o veículo da segunda perna inicia às 8h e o tempo de descarga é de 2 horas, o veículo da primeira perna precisa chegar ao ponto de apoio até as 6h. O tempo de descarga deve contemplar tanto a descarga em si quanto a preparação dos pedidos para a segunda perna.

![Imagem 3: Exemplo: se o veículo da segunda perna inicia às 8h e o tempo de descarga é de 2 horas, o veículo da primeira perna…](https://ajuda.sankhya.com.br/hc/article_attachments/44010954679831)

## Executando a roteirização

6. Com os cadastros realizados corretamente, inicie a roteirização pela **segunda perna**: selecione os pedidos e informe um ou mais veículos cadastrados para o ponto de apoio.

7. Com a rota da segunda perna criada, clique com o botão direito do mouse sobre o ponto de apoio e selecione uma das duas opções de transferência: **automática** ou **manual**.

![Imagem 4: 7. Com a rota da segunda perna criada, clique com o botão direito do mouse sobre o ponto de apoio e selecione uma das…](https://ajuda.sankhya.com.br/hc/article_attachments/44010966077463)

**7.1 — Transferência automática:** todos os pedidos que saem daquele ponto de apoio são incluídos automaticamente na rota de transferência. Basta selecionar um veículo diferente dos já utilizados na segunda perna e confirmar.

![Imagem 5: 7.1 — Transferência automática: todos os pedidos que saem daquele ponto de apoio são incluídos automaticamente na rota…](https://ajuda.sankhya.com.br/hc/article_attachments/44010984179095)

**7.2 — Transferência manual:** permite selecionar individualmente os pedidos que sairão do depósito com destino ao ponto de apoio. Após selecionar, clique em **"Criar nova rota"**, escolha o veículo e confirme a criação da rota de transferência.

![Imagem 6: 7.2 — Transferência manual: permite selecionar individualmente os pedidos que sairão do depósito com destino ao ponto…](https://ajuda.sankhya.com.br/hc/article_attachments/44010969987735)

8. As rotas da primeira e segunda perna são geradas na mesma sessão de roteirização. A partir daqui, siga com a sua operação de roteirização padrão.

![Imagem 7: 8. As rotas da primeira e segunda perna são geradas na mesma sessão de roteirização. A partir daqui, siga com a sua…](https://ajuda.sankhya.com.br/hc/article_attachments/44010984471063)

## Funcionalidade adicional — Intercalação de entregas na rota Last-Mile

O Routing possui um parâmetro que permite ao veículo da segunda perna (Last-Mile) **intercalar entregas a clientes finais durante o percurso de transferência**, sem precisar retornar ao ponto de apoio entre as paradas. Dessa forma, o mesmo veículo que realiza a distribuição pode aproveitar o trajeto para realizar entregas ao longo do caminho, tornando a operação mais eficiente.

Esse comportamento é controlado por um parâmetro configurável no **depósito ou na estratégia de roteirização**. Para ativá-lo, entre em contato com o suporte da Lincros pelo **Intercom** e solicite a habilitação dessa configuração no seu ambiente.

## Observações importantes

— Ao finalizar a roteirização, as rotas devem ser **exportadas individualmente**. As rotas de transferência são enviadas automaticamente ao depósito de destino via integração.

— Na segunda perna do processo, o tipo do conhecimento no TMS deve ser alterado para **"Redespacho"** ou **"Veículo Adicional"**.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos."
