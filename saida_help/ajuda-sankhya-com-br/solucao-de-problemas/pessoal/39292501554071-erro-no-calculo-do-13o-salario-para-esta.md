---
id: "39292501554071"
titulo: "Erro no cálculo do 13º salário para estagiários"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39292501554071-Erro-no-c%C3%A1lculo-do-13%C2%BA-sal%C3%A1rio-para-estagi%C3%A1rios"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:22:33Z"
rotulos: ["Configuração", "Folha de Pagamento", "Erro", "Artigo criado KCS", "Sankhya RH - KCS", "Estagiários", "Cadastro de Funcionários"]
---

# Erro no cálculo do 13º salário para estagiários

**MENSAGEM**

O sistema está calculando 13º salário para funcionários cadastrados como estagiários.

**SITUAÇÃO**

Ao processar a folha de pagamento, o sistema calcula indevidamente o 13º salário para colaboradores que possuem contrato de estágio. Esse cálculo aparece na folha mesmo que os funcionários estejam cadastrados com vínculo de estagiário.

**CAUSA**

O erro ocorre porque os estagiários estavam cadastrados com vínculo incorreto, como **"60 - Prazo Determinado"**. Funcionários com contrato de estágio não possuem direito ao 13º salário e não devem ter período de experiência configurado. Quando o vínculo está incorreto, o sistema interpreta que o colaborador tem direito ao benefício e realiza o cálculo indevidamente. Ao ajustar o cadastro para o vínculo correto de estagiário, o sistema deixa de calcular o 13º salário automaticamente.

**SOLUÇÃO**

Para corrigir o cálculo do 13º salário para estagiários, siga os passos abaixo:

**(1)** Acesse a tela **"Cadastro de Funcionários"** (Pessoal+ » Cadastros » Configuração Funcionários) e localize os colaboradores estagiários que estão com o cálculo incorreto.

**(2)** Verifique o campo **"Tipo de Vínculo"** no cadastro do funcionário.

![Imagem 1: Caso o vínculo esteja configurado como "60 - Prazo Determinado" ou outro vínculo incorreto, altere para o vínculo…](https://ajuda.sankhya.com.br/hc/article_attachments/41082044299799)

**(3)** Caso o vínculo esteja configurado como **"60 - Prazo Determinado"** ou outro vínculo incorreto, altere para o vínculo específico de **"Estagiário"**.

**(4)** Clique no **"Botão Salvar"** para gravar as alterações realizadas no cadastro do funcionário.

**(5)** Recalcule a folha de pagamento para que o sistema processe corretamente, sem incluir o 13º salário para os estagiários.

**Observações importantes:**

- Estagiários não têm direito ao 13º salário conforme a legislação brasileira.
- O vínculo correto deve ser sempre o específico para estagiários.
- Após o ajuste do vínculo, não é necessário realizar configurações adicionais.
- O sistema automaticamente deixará de calcular o 13º salário para esses colaboradores.
