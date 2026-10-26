---
id: "30948418365975"
titulo: "Veja como realizar a antecipação de reajuste salarial CCT"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30948418365975-Veja-como-realizar-a-antecipa%C3%A7%C3%A3o-de-reajuste-salarial-CCT"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:26:27Z"
rotulos: ["Configuração", "Ocorrências", "Parâmetros", "Folha de Pagamento", "Reajuste Salarial", "Passos para resolver", "Razão do erro", "Detalhe do erro", "antecipação de reajuste salarial CCT", "Convenção Coletiva"]
---

# Veja como realizar a antecipação de reajuste salarial CCT

A **antecipação de reajuste salarial na Convenção Coletiva de Trabalho** procura ajustar o salário dos trabalhadores antes do prazo estabelecido para o reajuste anual.

Para realizar o processo de antecipação, siga o passo a passo a seguir:

![Imagem 1: Na tela "Ocorrências" , aba "Cadastro" , verifique o cadastro da ocorrência 604 - ANTECIPAÇÃO REAJ. CCT.](https://ajuda.sankhya.com.br/hc/article_attachments/31541687862039) Na tela **"Ocorrências"**, aba **"Cadastro"**, verifique o cadastro da ocorrência 604 - ANTECIPAÇÃO REAJ. CCT.

- A marcação **"Ocorrência de reajuste sindical"** deve estar **desativada**, conforme exemplo:

![Imagem 2: A marcação "Ocorrência de reajuste sindical" deve estar desativada , conforme exemplo:](https://ajuda.sankhya.com.br/hc/article_attachments/31541644631831)
 

![Imagem 3: Na tela "Reajuste Salarial" , em "Lançar Reajuste" , preencha os campos:](https://ajuda.sankhya.com.br/hc/article_attachments/31541687862935) Na tela **"Reajuste Salarial"**, em **"Lançar Reajuste"**, preencha os campos:

- Empresa;
- Referência que será considerada para o reajuste;
- Percentual que será antecipado;
- Salário mínimo da classe
- No campo **"Histórico de Ocorrências"**, selecione a ocorrência **604 - Antecipação Reaj. CCT**

Após preencher todas as informações, em **"selecionar funcionários"**, selecione todos os funcionários que terão a antecipação.

O sistema permitirá a conferência dos valores com base no percentual informado, realize a conferência. Em seguida, clique em **"Efetivar".**
 
![Imagem 4: O sistema permitirá a conferência dos valores com base no percentual informado, realize a conferência. Em seguida,…](https://ajuda.sankhya.com.br/hc/article_attachments/31541644632855)

![Imagem 5: O sistema permitirá a conferência dos valores com base no percentual informado, realize a conferência. Em seguida,…](https://ajuda.sankhya.com.br/hc/article_attachments/31541644633367)

![Imagem 6: Quando houver a liberação da CCT, realize o cadastro na tela "Sindicato" com a % integral e informe os valores da…](https://ajuda.sankhya.com.br/hc/article_attachments/31541644634391) Quando houver a liberação da CCT, realize o cadastro na tela **"Sindicato"** com a % integral e informe os valores da antecipação nos campos:

- Perc. Antecipação;
- Data Ref. Antecipação;
- Cód. Hist. Antecipação = 604 - Antecipação Reaj. CCT

Com as informações preenchidas corretamente, o sistema irá considerar a antecipação para realizar o calculo da diferença dos valores.  

![Imagem 7: Com as informações preenchidas corretamente, o sistema irá considerar a antecipação para realizar o calculo da…](https://ajuda.sankhya.com.br/hc/article_attachments/31541687865111)

**Importante:** verifique os parâmetros a seguir. Pois, caso configurados incorretamente, podem impactar no processo de antecipação:

- **FPCODHISREA** - Cód. Hist. Ocorr. para Reajuste de Salário: este parâmetro contém a lista de códigos de ocorrências que podem ser utilizados no registro da ocorrência de uma alteração de salário. Confirme se o código 604 está inserido no parâmetro, caso não esteja, realize a inclusão.
- **FPREAJANTECIPA - Cód.Hist.Ocor. p/ Antecipação de Reajuste Sindical:** este parâmetro possui o código de ocorrência (604) utilizado para registro quando há uma antecipação do reajuste sindical, antes de sair a convenção coletiva oficial.
