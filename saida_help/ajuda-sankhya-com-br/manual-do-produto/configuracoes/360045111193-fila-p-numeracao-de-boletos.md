---
id: "360045111193"
titulo: "Fila p/ Numeração de Boletos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111193-Fila-p-Numera%C3%A7%C3%A3o-de-Boletos"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:57:36Z"
rotulos: ["manual", "Configuração", "Impressão", "Contas", "Fila", "Fila p/ Numeração de Boletos", "br.com.sankhya.com.cad.filanumeracaoboletas", "Fila p/ Numeração de Boletos manual", "Boleto", "Financeiro", "Numeração", "Gestão de Boletos: Simplificando a Impressão"]
---

# Fila p/ Numeração de Boletos

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310946772631) Módulo: Configurações > Cadastros
```

---

Nesta tela será definida a conta para a qual será impresso o boleto, bem como a faixa de numeração de boletos que será impresso.

![Imagem 2: Nesta tela será definida a conta para a qual será impresso o boleto, bem como a faixa de numeração de boletos que será…](https://ajuda.sankhya.com.br/hc/article_attachments/8926918091031)

Para efetuar o cadastro de uma nova **"Fila para Numeração de Boletos"**, após clicar no botão **"Novo"**, o usuário deverá informar:

O **"Nome da Fila"** e, no campo **"Conta"**, a conta para a qual será impresso o boleto.

Os campos **"Último boleto impresso"** e **"Último boleto no formulário"** deverão ser preenchidos com a faixa de numeração fornecida pelo banco.

**Nota:** no decorrer da impressão de boletos, o campo **"Último boleto no formulário"** será acrescentado pelo sistema de forma automática.

## Processo de impressão por fila:

1.Definir a conta e a faixa de numeração para impressão do boleto na tela Fila p/ Numeração de Boletos;

2.No [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abaidentificao), no campo **"Nome Fila p/ num.Boleto"**, definir qual fila o usuário utilizará na impressão.

Se o parâmetro **"Controla boleto por fila? - FILABOLETA"** estiver ligado e o usuário tiver uma fila de impressão cadastrada, o sistema utilizará a impressora da Fila para imprimir os mesmos. Caso contrário, ou seja, se o usuário não tiver nenhuma Fila de impressão, o sistema buscará a impressora da Conta registrada no financeiro da nota.

Se os títulos da nota não possuírem o Nosso Número ou o parâmetro **"Renumera nosso número sempre ? - RENNOSSONUM"** estiver ligado juntamente com o parâmetro FILABOLETA, no momento da impressão do boleto, a Conta e o Banco registrados no financeiro serão substituídos pela Conta e Banco cadastrados na Fila.

Neste caso o Modelo utilizado para impressão do boleto será o da Conta da Fila.

**Observação:** o Sankhya Om utiliza para impressão um Relatório Formatado, sendo que, a [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) busca o modelo de impressão na tela [Modelos de Nota Fiscal/Duplicatas/Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913-Modelos-de-Nota-Fiscal-Duplicatas-Boleto-s-), que deverá estar vinculado a um modelo configurado na tela [Modelos de Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607134-Modelos-de-Boleto-s-).

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111193-Fila-p-Numera%C3%A7%C3%A3o-de-Boletos#top)
