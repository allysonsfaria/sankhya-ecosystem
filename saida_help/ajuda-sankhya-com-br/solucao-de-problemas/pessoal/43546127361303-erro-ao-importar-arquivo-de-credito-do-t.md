---
id: "43546127361303"
titulo: "Erro ao importar arquivo de crédito do trabalhador (\"Não há funcionário cadastrado com o CPF, matrícula e data admissão informados\")"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43546127361303-Erro-ao-importar-arquivo-de-cr%C3%A9dito-do-trabalhador-N%C3%A3o-h%C3%A1-funcion%C3%A1rio-cadastrado-com-o-CPF-matr%C3%ADcula-e-data-admiss%C3%A3o-informados"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-09-18T11:09:44Z"
rotulos: ["Artigo criado KCS", "Sankhya RH - KCS"]
---

# Erro ao importar arquivo de crédito do trabalhador ("Não há funcionário cadastrado com o CPF, matrícula e data admissão informados")

**MENSAGEM**

Não há funcionário cadastrado com o CPF, matrícula e data admissão informados.

**SITUAÇÃO**

A mensagem ocorre ao tentar importar a planilha de crédito do trabalhador (eConsignado) na tela **"Lançamento de Movimentos"** (Rotinas Folha Lançamento de Movimentos), utilizando o arquivo baixado do Portal Emprega Brasil. O erro é apresentado para um ou mais funcionários, mesmo que estejam ativos no sistema e que a importação tenha funcionado normalmente em meses anteriores.

### Causas Comuns

- Divergência entre os dados do arquivo (CPF, matrícula, data de admissão) e o cadastro do funcionário no Sankhya.
- Data de admissão diferente entre o sistema e o arquivo do eSocial/Emprega Brasil.
- Funcionário transferido entre empresas com datas de transferência duplicadas ou inconsistentes.
- Cadastro do banco não existente ou inativo no sistema.
- Número do contrato do crédito consignado não informado.

**SOLUÇÃO**

**(1)** Acesse a planilha que está sendo importada e identifique os funcionários que apresentaram erro na importação.

**(2)** Verifique se os dados de **"CPF"**, **"matrícula"** e **"data de admissão"** desses funcionários na planilha estão exatamente iguais aos dados cadastrados no sistema. Para isso, acesse a tela **"Configuração Funcionário"** (Pessoal+ » Cadastros » Configuração Funcionários).

**(3)** Caso identifique divergência em algum dos dados, ajuste manualmente a informação na planilha para que fique igual ao cadastro do sistema.

- Confira se o **CPF**, **matrícula** e **data de admissão** estão exatamente iguais aos informados no arquivo de importação.
- Se houver divergência na data de admissão, consulte o portal do eSocial para confirmar a data original do vínculo.
- Corrija no cadastro do funcionário no Sankhya, se o erro estiver no sistema.
- Após o ajuste, envie a retificação ao eSocial para manter a consistência das informações.
- Se a data estiver correta tanto no eSocial quanto no sistema, entre em contato com a instituição responsável pelo arquivo (por exemplo, Emprega Brasil) para verificar a origem da divergência.
- Verifique se todos os bancos informados na planilha estão cadastrados e ativos no sistema.
- Cadastre bancos ausentes antes de tentar nova importação.
- Acesse o cadastro do funcionário e confira as **Datas de Transferência** entre empresas.
- Certifique-se de que não há duplicidade de datas (origem e destino iguais).
- Mantenha apenas a data de transferência válida para a empresa de destino.

**(4)** Salve a planilha corrigida e realize novamente a importação na tela **"Lançamento de Movimentos"**. Pessoal+ » Rotinas Folha » Lançamento de Movimento

**(5)** Se o erro persistir, valide se no Portal Emprega Brasil a data de admissão está correta. Caso esteja divergente, oriente a abertura de chamado junto ao Emprega Brasil para correção da informação.

---

### Resumo dos Pontos de Atenção

- Os dados do funcionário (CPF, matrícula, data de admissão) devem ser idênticos no sistema e no arquivo.
- Ajuste divergências de data de admissão e envie retificação ao eSocial, se necessário.
- Verifique transferências entre empresas e evite datas duplicadas.
- Confirme o cadastro dos bancos e o preenchimento do número do contrato.
- Utilize sempre a planilha correta e atualizada.

**CAUSA**

A causa do erro é a divergência entre os dados de **"CPF"**, **"matrícula"** e/ou **"data de admissão"** informados na planilha de importação e os dados cadastrados no sistema. Frequentemente, a divergência ocorre na data de admissão, principalmente em casos de funcionários transferidos, onde o arquivo do governo pode trazer a data de transferência ao invés da data de admissão original. O sistema exige que os três campos estejam idênticos para realizar a importação corretamente.
