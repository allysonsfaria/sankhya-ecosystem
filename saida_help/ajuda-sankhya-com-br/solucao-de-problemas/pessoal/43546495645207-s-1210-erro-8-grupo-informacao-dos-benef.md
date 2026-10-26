---
id: "43546495645207"
titulo: "S-1210 - Erro 8 - Grupo 'Informação dos beneficiários da pensão alimentícia' deve ser preenchido."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43546495645207-S-1210-Erro-8-Grupo-Informa%C3%A7%C3%A3o-dos-benefici%C3%A1rios-da-pens%C3%A3o-aliment%C3%ADcia-deve-ser-preenchido"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-10-05T18:57:25Z"
rotulos: ["Artigo criado KCS", "Sankhya RH - KCS"]
---

# S-1210 - Erro 8 - Grupo 'Informação dos beneficiários da pensão alimentícia' deve ser preenchido.

**MENSAGEM**

"Erro 8" - Grupo 'Informação dos beneficiários da pensão alimentícia' deve ser preenchido.

**SITUAÇÃO**

O erro ocorre ao tentar enviar o evento **"S-1210"** ao eSocial, quando há desconto de pensão alimentícia para um ou mais dependentes, mas as informações obrigatórias desses beneficiários não estão devidamente cadastradas ou vinculadas no sistema. Isso pode acontecer tanto em folhas normais quanto em folhas de décimo terceiro salário.

**SOLUÇÃO**

**(1)** Acesse a tela **"Configuração Funcionários"** Pessoal+ » Cadastros » Configuração Funcionários e selecione o colaborador que possui desconto de pensão alimentícia.

**(2)** Na aba **"Dependentes"**, localize o dependente que recebe a pensão e clique para editar.

**(3)** Na sub-aba **"Dados da Pensão"**, preencha obrigatoriamente:

- Marque o dependente como **"Pensionista"**;
- Informe o **"Parceiro responsável pelo recebimento da pensão"**;
- Cadastre o(s) evento(s) de desconto de pensão utilizados na folha;
- Se houver mais de um dependente pensionista, cadastre os eventos individualmente para cada um.

**(4)** Salve o cadastro do dependente.

**(5)** Acesse a tela **"Lançamento de Movimento"** (Pessoal+ Rotinas Folha Lançamento de Movimento) e confira se o evento de desconto de pensão está lançado corretamente para o dependente na referência desejada.

**(6)** Bloqueie e libere novamente a folha no **"Gerenciador de Folhas"** (Pessoal+ Rotinas Folha Gerenciador de Folhas).

**(7)** Reenvie o evento **"S-1210"** pela **"Central do eSocial"** (Pessoal+ Rotinas Folha Central do eSocial).

Artigo relacionado:

https://ajuda.sankhya.com.br/hc/pt-br/articles/33792842489623-Cadastro-de-Dependente-para-Pens%C3%A3o-Aliment%C3%ADcia

**Dicas importantes:**

- Sempre utilize a tela **"Configuração Funcionários"** para cadastrar e vincular informações de pensão, evitando lançamentos manuais apenas pela tela **"Lançamento de Movimento"**.
- O preenchimento do **"Parceiro responsável pelo recebimento da pensão"** é obrigatório para o correto envio ao eSocial.
- Certifique-se de que a sequência do dependente está correta no cadastro, lançamento e cálculo da folha.

**CAUSA**

O erro ocorre porque o sistema identificou desconto de pensão alimentícia na folha, mas não encontrou todas as informações obrigatórias do grupo **"penAlim"** para o dependente: falta marcar o dependente como pensionista, informar o parceiro responsável, cadastrar o evento de desconto ou garantir que o dependente está corretamente vinculado e enviado ao eSocial. Sem esses dados, o evento **"S-1210"** não consegue montar o grupo de informações dos beneficiários da pensão alimentícia, gerando o erro 8.
