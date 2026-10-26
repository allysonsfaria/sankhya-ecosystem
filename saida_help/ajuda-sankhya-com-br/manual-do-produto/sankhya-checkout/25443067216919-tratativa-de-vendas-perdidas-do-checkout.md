---
id: "25443067216919"
titulo: "Tratativa de Vendas Perdidas do Checkout no Sankhya Om"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25443067216919-Tratativa-de-Vendas-Perdidas-do-Checkout-no-Sankhya-Om"
trilha: "Manual do Produto > Comercial e Vendas > Vendas > Sankhya Checkout"
atualizado_em: "2026-07-29T16:02:54Z"
rotulos: ["Configuração", "Sefaz", "Vendas", "NFC-e", "Sankhya Checkout", "Top p/ vendas Perdidas no Checkout!", "TOPVDPDCHECKOUT", "Tratativa de Vendas Perdidas do Checkout no Sankhya Om", "Gerente do financeiro", "Gerente de caixa", "Sankhya Om", "Documentos Eletrônicos"]
---

# Tratativa de Vendas Perdidas do Checkout no Sankhya Om

Quando o sistema Sankhya tiver o produto [Checkout](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595394) na sua licença e o usuário for indicado como **"Gerente de caixa"** ou **"Gerente do financeiro"** (tela [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874), aba [Segurança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abasegurana)) poderá realizar as tratativas de vendas perdidas no Checkout.

Todas as vendas perdidas no Checkout por falhas de comunicação serão levadas para a tela inicial do **Sankhya Om** e com isso o usuário responsável poderá tomar a decisão de cancelar, inutilizar ou o que for melhor, segundo sua análise.

![Imagem 1: Todas as vendas perdidas no Checkout por falhas de comunicação serão levadas para a tela inicial do Sankhya Om e com…](https://ajuda.sankhya.com.br/hc/article_attachments/26815917738519)

Esse fluxo traz os seguintes benefícios:

- **Centralização de Notas Pendentes**: todas as notas com problemas são centralizadas no **Sankhya Om** para tratamento.
- **Notificação Proativa**: o Gerente de caixa será notificado imediatamente sobre as notas pendentes, permitindo ações rápidas.
- **Facilidade de Acesso e Tratamento**: o [Portal de Caixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/7317826345367) ou o [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654) fornece uma interface centralizada e filtrada para tratar as notas pendentes.
- **Redução de Abertura de Tickets**: menos necessidade de abrir tickets no Service Desk, pois as notas podem ser tratadas diretamente pelo Gerente de caixa.
- **Eficiência Operacional**: melhor coordenação e resolução de problemas com menos impacto nas operações diárias.

### Imagem 2: Operação Diária no Checkout Operação Diária no Checkout

**(2)Operador de Caixa**:

- - Realiza vendas e emite NFC-e normalmente.

(2)** Sistema Checkout**:

- - Emite as notas fiscais conforme as melhorias implementadas no robô de emissão de notas;
  - Se houver falha de comunicação com a Sefaz, gera um registro na tabela TNRVENDAPERDIDO.

### Imagem 3: Identificação de Nota Perdida Identificação de Nota Perdida

**(2)** **Sistema Checkout**:

- - Detecta falha na comunicação com a Sefaz e registra na tabela TNRVENDAPERDIDO;
  - Importa automaticamente a venda para o **Sankhya Om** usando uma [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) específica configurada para notas perdidas;
  - Configura a TOP no parâmetro **"Top p/ vendas Perdidas no Checkout! - TOPVDPDCHECKOUT"**. Sabendo que, essa TOP deve ser cadastrada para não gerar lançamentos financeiros e de estoque.

(1)** Quando TOP não configurada**

(2)** Sistema Checkout**:

- - Mesmo sem a TOP configurada é enviado a nota para **Sankhya Om** ficando pendente na tela [Administração do Checkout](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050978053).

(2)** Sistema Sankhya Om**:

- - Envia uma notificação para o usuário indicado como Gerente de caixa e Gerente do financeiro com a seguinte mensagem:

**“Existe pendência de notas para serem sincronizadas, consulta à tela Administração de Checkout.”**

- - Na tela Administração de Checkout, no menu [Importação de Movimentações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050978053-Administra%C3%A7%C3%A3o-de-Checkout#abaimporta%C3%A7%C3%A3odemovimenta%C3%A7%C3%B5es) será apresentado cada registro de nota perdido que não foi integrado com a seguinte mensagem:

**“TOP não configurada no parâmetro TOPVDPDCHECKOUT”**

- - Após configurar uma TOP de venda, destaca-se que não deve gerar problemas financeiros e estoque, mas, voltar na tela Administração de Checkout para reprocessar as linhas e assim seguir com a integração;
  - Executa o job **"ImportaDadosJob"** cadastrado na tela [Controle de Jobs](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594634), processando as integrações pendentes do Checkout rotineiramente com o tempo de execução de aproximadamente 1min.

### Imagem 4: Sincronização e Notificação no Sankhya Om Sincronização e Notificação no Sankhya Om

(2)** Sistema Sankhya Om**:

- - Recebe a nota perdida com a TOP configurada;
  - Envia uma notificação para o usuário indicado como Gerente de caixa e Gerente do financeiro com a seguinte mensagem:

**“Título: Nota Perdida no Checkout X da Loja Y**

**Foi identificada uma nota perdida no Checkout X cod. empresa Y.**

**Observação: A nota de número XPTO, referente à venda Y, necessita de tratativa. Solicitamos que consultem essa nota no Portal de Caixa/Portal de Vendas para as devidas providências. Como dica, utilize o filtro pelo tipo de operação do parâmetro X de notas perdidas no checkout.”**

(1)** Job automático para processamento da Nota na Sefaz**

(2)** Sistema Sankhya Om**:

- - Existe um job X que será executado de Y (Tempo) que fará a consulta de status da nota sincronizada. 
    - Se não existir dados na Sefaz, irá inutilizar a faixa da série e excluir o tipo de movimento;
    - Caso exista na Sefaz, atualizará o status da nota como **"Aprovada"** e fará a tentativa de cancelamento;
      - Se não conseguir cancelar devido ao prazo de 30 min ou outra situação, o usuário deve tomar a decisão junto sua contabilidade e executar ação no [Portal de Caixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/7317826345367) ou [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654).

### Imagem 5: Acesso ao Portal de Caixa ou Portal de Vendas Acesso ao Portal de Caixa ou Portal de Vendas

(2)** Gerente de caixa ou Gerente do financeiro**:

- - Recebe a notificação sobre a nota perdida;
  - Acessa o Portal de Caixa ou Portal de Vendas no **Sankhya Om** para visualizar as notas pendentes quando o job citado no passo anterior não conseguir resolver a nota;
  - Utiliza filtros (por exemplo, tipo de operação e empresa/loja) para localizar a nota perdida.

### Imagem 6: Tratativa da Nota Perdida Tratativa da Nota Perdida

(2)** Gerente de caixa ou Gerente do financeiro**:

- - Seleciona a nota pendente para análise;
  - Decide a ação a ser tomada conforme as seguintes opções:
    - **Cancelamento Extemporâneo**: esta opção cancela a nota após o prazo regular, se aplicável;
    - **Outras Ações**: esta opção deve ser selecionada em caso de devolução ou regularização.

![Imagem 7: Para saber detalhes sobre o Cancelamento Extemporâneo , acesse o link Como realizar um cancelamento extemporâneo? .](https://ajuda.sankhya.com.br/hc/article_attachments/26834217810967) Para saber detalhes sobre o Cancelamento Extemporâneo, acesse o link [Como realizar um cancelamento extemporâneo?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042624054).

### Imagem 8: Atualização e Conclusão Atualização e Conclusão

(2)** Sistema Sankhya Om**:

- - Atualiza o status da nota conforme a ação tomada pelo Gerente de caixa ou Gerente do financeiro;
  - Sincroniza as alterações com o sistema Checkout para manter a consistência dos dados.
