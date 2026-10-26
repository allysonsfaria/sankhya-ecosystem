---
id: "44011200139543"
titulo: "[TMS] - Como cadastrar um componente de Agendamento de Entrega"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011200139543--TMS-Como-cadastrar-um-componente-de-Agendamento-de-Entrega"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T18:58:29Z"
rotulos: ["sync_hc", "lincros", "lincros_13438977", "sync_hash_2ebd040e4bf2"]
---

# [TMS] - Como cadastrar um componente de Agendamento de Entrega

**Menu**: Cadastros Gerais > Configurações de empresa > Componentes de frete

**Objetivo**: Como realizar o cadastro de um componente de frete de 'Agendamento de Entrega' onde o cálculo é sobre o valor do frete

**Considerações**:

- Possuir acesso ao menu dos componentes de frete e tipos de movimentos;

Abaixo segue os procedimentos necessários:

Neste exemplo do componente o mesmo será calculo sobre o valor do frete tendo um percentual e um valor mínimo:

1. Acessar o menu: Cadastros Gerais > Configurações de empresa > Tipos de movimento
2. Realizar o cadastro do tipo de movimento, conforme exemplo abaixo, clicando na opção 'Novo':

**Código**: Informe um número para este tipo de movimento;

**Nome**: Informe o nome para o tipo de movimento;

**Tipo**: Selecione a opção 'Cálclo de frete por Tabela';

![Imagem 1: Tipo : Selecione a opção 'Cálclo de frete por Tabela';](https://ajuda.sankhya.com.br/hc/article_attachments/44011190732183)

3. Após o cadastramento do tipo de movimento, acessar o menu: Cadastros Gerais > Configurações de empresa > Componentes de frete;

4. Clicar na opção 'Novo';

5. Informar os dados abaixo:

**Código**: Informar o código para este componente de frete;

**Tipo de Cálculo:** Selecionar a opção 'Frete';

**Descrição**: Informar uma breve descrição para este componente;

**Fórmula de cálculo**: Informar a fórmula de cálculo conforme abaixo:

Formula: valor = new Double(((FP \* PERCENTUAL)) / 100.0    );

if (valor < VALOR\_MINIMO) {

   valor = VALOR\_MINIMO;

}

return valor;

**Ordem de Exibição:**Informar qual será a ordem de exibição deste componente;

**Código movimento**: Informar o código do movimento criado acima em 'Tipo de Movimento';

Selecionar as opções abaixo:

![Imagem 2: Selecionar as opções abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/44011208729239)

6. Clicar em 'Salvar';

Abaixo segue um print de como ficará o cadastro deste componente:

![Imagem 3: Abaixo segue um print de como ficará o cadastro deste componente:](https://ajuda.sankhya.com.br/hc/article_attachments/44011200709783)

Após será necessário realizar o cadastramento este componente na tabela de fretes em questão, informando o percentual e o valor mínimo a ser calculado.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
