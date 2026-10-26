---
id: "39365426070807"
titulo: "Erro ao emitir TRCT de rescisão complementar"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39365426070807-Erro-ao-emitir-TRCT-de-rescis%C3%A3o-complementar"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-10-19T19:58:38Z"
rotulos: ["Configuração", "Eventos", "Folha de Pagamento", "Rescisão", "Erro", "TRCT", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Erro ao emitir TRCT de rescisão complementar

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39365426067223) **Mensagem**

Relatório de rescisão não pode ser gerado pois os eventos não estão configurados.

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39365426067351) **Situação**

Após realizar o cálculo de uma rescisão complementar, o documento **"TRCT"** (Termo de Rescisão de Contrato de Trabalho) não fica disponível para emissão. Ao tentar gerar o relatório, o sistema apresenta mensagem informando que determinados eventos calculados na rescisão não estão configurados para aparecer no documento.

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39365426067479) **Solução**

Para resolver este problema, configure os eventos que foram calculados na rescisão complementar. Existem duas formas de realizar esta configuração:

**Configurar o evento na Regra de Cálculo**

![Imagem 4: Acesse a tela "Regras de Cálculo" (Pessoal+ >> Configurações >> Regras de Cálculo).](https://ajuda.sankhya.com.br/hc/article_attachments/39365426067607) Acesse a tela **"Regras de Cálculo"** (Pessoal+ >> Configurações >> Regras de Cálculo).

![Imagem 5: Selecione a regra utilizada na empresa do funcionário e clique no botão "Editar" .](https://ajuda.sankhya.com.br/hc/article_attachments/39365426067735) Selecione a regra utilizada na empresa do funcionário e clique no botão **"Editar"**.

![Imagem 6: Acesse a aba "TRCT" e depois a sub-aba "Eventos" .](https://ajuda.sankhya.com.br/hc/article_attachments/39365426067863) Acesse a aba **"TRCT"** e depois a sub-aba **"Eventos"**.

![Imagem 7: Localize o campo apropriado onde o evento deve ser inserido. Verifique se é um provento ou desconto e dê um duplo…](https://ajuda.sankhya.com.br/hc/article_attachments/39365426067991) Localize o campo apropriado onde o evento deve ser inserido. Verifique se é um provento ou desconto e dê um duplo clique no campo desejado.

![Imagem 8: No quadro de eventos que aparecer, clique no botão "+" e adicione o evento que está gerando o erro.](https://ajuda.sankhya.com.br/hc/article_attachments/39365433974039) No quadro de eventos que aparecer, clique no botão **"+"** e adicione o evento que está gerando o erro.

![Imagem 9: Salve as alterações e tente gerar o "TRCT" novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/39365433974167) Salve as alterações e tente gerar o **"TRCT"** novamente.

![Imagem 10: Salve as alterações e tente gerar o "TRCT" novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/41052931650583)

**Observações importantes:**

- Certifique-se de adicionar o evento no local correto (Proventos ou Descontos). Se tentar inserir um provento na seção de descontos (ou vice-versa), o sistema emitirá um alerta.
- Alguns campos do **"TRCT"** possuem descrição padrão e não podem ser alterados, pois seguem a Portaria 1057 do Ministério do Trabalho.
- Os campos em branco podem receber qualquer descrição e código de evento que não esteja previsto na legislação.
- Após realizar a configuração, tente gerar o relatório novamente para verificar se o problema foi resolvido.

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39365433974423) **Causa**

O erro ocorre porque os eventos pagos na rescisão complementar não estavam cadastrados na **"Regra de Cálculo"**, especificamente na aba **"TRCT"**. Quando um evento é calculado na rescisão mas não está configurado para aparecer no documento, o sistema impede a geração do relatório para garantir que todas as informações sejam apresentadas corretamente no termo de rescisão.
