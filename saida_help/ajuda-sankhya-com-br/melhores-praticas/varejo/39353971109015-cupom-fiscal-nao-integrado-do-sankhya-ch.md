---
id: "39353971109015"
titulo: "Cupom fiscal não integrado do Sankhya Checkout para o Sankhya/W"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39353971109015-Cupom-fiscal-n%C3%A3o-integrado-do-Sankhya-Checkout-para-o-Sankhya-W"
trilha: "Melhores Práticas > Varejo"
atualizado_em: "2026-07-22T13:50:33Z"
rotulos: ["Configuração", "SEFAZ", "Integração", "Sankhya Checkout", "Erro", "Artigo criado KCS", "Varejo - KCS"]
---

# Cupom fiscal não integrado do Sankhya Checkout para o Sankhya/W

**SITUAÇÃO**

Essa situação ocorre quando uma venda é finalizada no Sankhya Checkout e a NFC-e é autorizada com sucesso pela SEFAZ. Entretanto, durante o processo de integração com o ERP Sankhya, o sistema não consegue localizar ou processar corretamente o documento fiscal correspondente.

Como consequência, a NFC-e permanece registrada apenas no Sankhya Checkout, sem que o documento seja integrado e disponibilizado no ERP Sankhya, gerando divergência entre os ambientes e impedindo o gerenciamento da venda pelo ERP.

Antes de iniciar análises mais aprofundadas, é importante verificar se o tempo configurado em **Menu > Preferências**, na aba **Integração**, no campo **"Intervalo de Integração com o ERP (Minutos)"**, já foi ultrapassado.

![Imagem 1: Antes de iniciar análises mais aprofundadas, é importante verificar se o tempo configurado em Menu > Preferências , na…](https://ajuda.sankhya.com.br/hc/article_attachments/41173763420823)

A integração entre o Sankhya Checkout e o ERP Sankhya ocorre automaticamente conforme o intervalo definido nesse parâmetro. Portanto, caso o período configurado ainda não tenha sido atingido, é esperado que a venda permaneça apenas no Sankhya Checkout até a próxima execução da rotina de integração.

**SOLUÇÃO**

**(1)** Acessar a tela **Administração do Checkout** (**Configurações >> Sankhya Checkout**) e verificar a aba **"Importações de Movimentação"**.

Todas as vendas originadas no Sankhya Checkout passam por essa tela antes de serem totalmente integradas ao ERP. Portanto, é importante verificar se a venda em questão permanece registrada nessa listagem.

Caso a venda esteja presente na aba **Importações de Movimentação**, será possível identificar os erros que impediram a conclusão da integração, pois a própria tela apresenta as ocorrências relacionadas ao processo.

![Imagem 2: Localize o cupom fiscal que não foi integrado ao ERP e verifique se existe alguma mensagem de erro associada ao…](https://ajuda.sankhya.com.br/hc/article_attachments/41173746782615)

**(2)** Localize o cupom fiscal que não foi integrado ao ERP e verifique se existe alguma mensagem de erro associada ao registro.

Caso o cupom esteja listado na tela, analise a descrição da ocorrência apresentada pelo sistema, pois ela indicará o motivo pelo qual a integração não foi concluída com sucesso.

Com base na mensagem identificada, realize a tratativa necessária para corrigir a inconsistência apontada.

**(3)** Após corrigir a causa do erro, selecione o registro da venda e clique na opção: **"Reprocessar Movimentação Selecionada"**

O sistema realizará uma nova tentativa de integração do cupom fiscal com o ERP Sankhya.

Após o reprocessamento, valide se o documento foi integrado com sucesso e se já está disponível normalmente no Portal de Venda no ERP Sankhya.
