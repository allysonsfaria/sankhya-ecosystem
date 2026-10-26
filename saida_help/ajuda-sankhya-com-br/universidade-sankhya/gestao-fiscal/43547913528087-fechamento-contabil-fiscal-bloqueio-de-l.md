---
id: "43547913528087"
titulo: "Fechamento contábil/fiscal: bloqueio de lançamentos futuros e melhores práticas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43547913528087-Fechamento-cont%C3%A1bil-fiscal-bloqueio-de-lan%C3%A7amentos-futuros-e-melhores-pr%C3%A1ticas"
trilha: "Universidade Sankhya > Gestão Fiscal"
atualizado_em: "2026-10-07T14:14:24Z"
rotulos: ["Artigo criado KCS", "Fiscal/Contábil - KCS"]
---

# Fechamento contábil/fiscal: bloqueio de lançamentos futuros e melhores práticas

A **"Configuração Fechamento contábil/fiscal"** impede lançamentos retroativos e garante a integridade das informações no ERP Sankhya.

A **"Configuração Fechamento contábil/fiscal"** é uma funcionalidade essencial no ERP Sankhya para garantir a integridade dos dados fiscais e contábeis. Ao realizar o fechamento de um período, o sistema bloqueia automaticamente qualquer tentativa de lançamento, edição ou exclusão de documentos que afetem as áreas contábil e fiscal com datas anteriores à data de fechamento definida. Dessa forma, evita-se alterações indevidas em períodos já encerrados, protegendo a consistência das informações e atendendo exigências legais e de auditoria.

A configuração do fechamento deve ser feita com cautela, pois, uma vez ativada, não pode ser desfeita. O bloqueio é aplicado de forma geral, abrangendo rotinas de estoque, financeiro, contábil e fiscal. Caso haja necessidade de bloqueios específicos, recomenda-se avaliar a possibilidade de personalização junto à equipe de implantação.

### Como funciona o bloqueio após o fechamento

O fechamento impede lançamentos, edições e exclusões retroativas.

Após a configuração do **"Configuração Fechamento contábil/fiscal"**, o sistema bloqueia automaticamente qualquer movimentação que envolva datas anteriores à data de fechamento. Isso inclui:

- Lançamento de novos documentos fiscais, financeiros, contábeis ou de estoque com data retroativa;
- Edição ou exclusão de documentos já lançados em períodos fechados;
- Impossibilidade de alterar campos como **"Dt. Entrada/Saída"** e **"Dt. Movimento"** para datas anteriores ao fechamento.

Essas restrições são fundamentais para evitar inconsistências e garantir que os dados enviados ao Fisco ou utilizados em demonstrações contábeis permaneçam íntegros.

### Configuração do fechamento contábil/fiscal

O fechamento deve ser configurado com atenção e planejamento.

Para configurar o fechamento, acesse a tela **"Configuração Fechamento Contábil/Fiscal"** (Livros Fiscais » Contabilidade » Configuração Fechamento Contábil/Fiscal). Defina a data limite para lançamentos e confirme a operação. Recomenda-se realizar essa configuração em conjunto com a equipe responsável pela implantação, pois o processo é irreversível.

O bloqueio será aplicado a todas as áreas integradas ao fechamento. Caso a empresa precise de um controle mais granular, como bloquear apenas lançamentos fiscais ou de estoque, avalie a viabilidade de uma personalização.

Mais detalhes de Configuração acesse o link [Configuração Fechamento Contábil/Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595654-Configura%C3%A7%C3%A3o-Fechamento-Cont%C3%A1bil-Fiscal)

### Boas práticas para o fechamento contábil/fiscal

Planeje o fechamento e oriente os usuários para evitar retrabalho.

Antes de realizar o fechamento, oriente os usuários a revisar e regularizar todos os lançamentos do período. Certifique-se de que não há pendências de notas fiscais, ajustes financeiros ou movimentações de estoque em aberto. Após o fechamento, qualquer ajuste necessário deverá ser feito por meio de lançamentos em períodos abertos, utilizando documentos de ajuste, devolução ou regularização conforme a necessidade e orientação contábil.

Mantenha uma rotina periódica de fechamento (mensal, trimestral ou anual, conforme a política da empresa) e registre todas as operações para facilitar auditorias e eventuais revisões.
