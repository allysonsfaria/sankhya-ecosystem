---
id: "43547980419735"
titulo: "Melhores práticas para implantação de saldo em contas contábeis"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43547980419735-Melhores-pr%C3%A1ticas-para-implanta%C3%A7%C3%A3o-de-saldo-em-contas-cont%C3%A1beis"
trilha: "Manual do Produto > Fiscal e Contábil > Contábil"
atualizado_em: "2026-09-24T20:05:17Z"
rotulos: ["Artigo criado KCS", "Fiscal/Contábil - KCS"]
---

# Melhores práticas para implantação de saldo em contas contábeis

A implantação de saldo em contas contábeis é uma etapa fundamental para garantir a integridade dos dados contábeis ao iniciar a utilização do ERP Sankhya ou ao realizar ajustes de abertura de exercícios. Este processo consiste em registrar os saldos iniciais das contas do plano de contas, permitindo que os relatórios contábeis reflitam corretamente a posição patrimonial e de resultado da empresa desde o início do período contábil.

Para garantir a correta implantação dos saldos, é necessário seguir uma rotina padronizada, observando a estrutura do plano de contas, a classificação das contas (ativo, passivo, resultado, etc.) e a correta utilização das telas e campos do sistema. A seguir, apresentamos as melhores práticas para realizar este procedimento de forma segura e eficiente.

### Preparação do ambiente contábil

Antes de iniciar a implantação dos saldos, certifique-se de que o plano de contas está devidamente cadastrado e estruturado na tela **"Plano de Contas** (Contabilidade » Cadastros). Verifique se todas as contas necessárias estão criadas, classificadas corretamente no campo **"Grupo de Conta"** e, se aplicável, vinculadas ao plano de contas referencial na aba **"Conta Contábil Referencial"**.

Além disso, confira se a empresa está configurada corretamente na tela **Empresa** (Contabilidade » Preferências), com o período contábil de abertura devidamente informado na aba **"Exercício"**. Isso garantirá que os lançamentos de implantação sejam realizados no período correto.

### Procedimento para implantação dos saldos

Para realizar a implantação dos saldos, siga o passo a passo abaixo:

**(1)** Acesse a tela **Lotes Contábeis** (Contabilidade » Arquivos) e selecione a empresa e o período de abertura do exercício contábil. Crie um novo lote informando: Nro. Lote, Referência e Dt. Movimento.
**(2)** Acesse a tela **Lançamentos contábeis** (Contabilidade » Arquivos) e selecione a empresa e o período de abertura do exercício contábil.
**(3)** Crie um novo lançamento, informando no campo **"Data do Movimento"** a data de início do período contábil (normalmente o primeiro dia do exercício).
**(4)**No campo **"Histórico"**, utilize uma descrição que identifique o lançamento como implantação de saldo, por exemplo: "Implantação de saldo inicial".
**(5)** Garanta que o lançamento fique **totalmente equilibrado** (soma dos débitos igual à soma dos créditos), evitando diferenças que possam comprometer o balancete.

**(6)**Salve e confirme o lançamento. Repita o procedimento para todas as empresas ou exercícios que necessitem de implantação de saldo.

Caso utilize centros de resultado ou projetos, distribua os saldos conforme a necessidade, preenchendo os campos correspondentes em cada linha do lançamento.

Após a implantação, utilize o relatório **Balancete de Verificação** (Contabilidade » Consultas) para conferir se os saldos foram lançados corretamente e se o balancete está equilibrado.

###

### Cuidados e validações após a implantação

Após concluir a implantação dos saldos, realize as seguintes validações:

Gere o **"Balancete"** e confira se o somatório do ativo está igual ao do passivo, incluindo o patrimônio líquido.
Verifique se todas as contas relevantes receberam saldo e se não há contas com saldo indevido.
Caso identifique diferenças, revise os lançamentos de implantação e ajuste conforme necessário.

Lembre-se de que a correta implantação dos saldos é essencial para a geração de relatórios contábeis, ECD, ECF e demais obrigações acessórias. Recomenda-se documentar o procedimento realizado e manter os comprovantes dos saldos implantados para futuras auditorias.

Seguindo estas melhores práticas, a implantação de saldo em contas contábeis será realizada de forma segura, garantindo a integridade e confiabilidade das informações contábeis no ERP Sankhya.
