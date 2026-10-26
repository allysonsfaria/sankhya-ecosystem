---
id: "33647481317783"
titulo: "Não existe convenção coletiva com cálculo de dissídio pendente para esta referência"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33647481317783-N%C3%A3o-existe-conven%C3%A7%C3%A3o-coletiva-com-c%C3%A1lculo-de-diss%C3%ADdio-pendente-para-esta-refer%C3%AAncia"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:20:13Z"
rotulos: ["Configuração", "Folha de Pagamento", "Dissídio", "Reajuste Salarial", "Não existe convenção", "coletiva com cálculo de dissídio", "pendente para esta referência", "Erro"]
---

# Não existe convenção coletiva com cálculo de dissídio pendente para esta referência

**MENSAGEM**

Não existe convenção coletiva com cálculo de dissídio pendente para esta referência

**SITUAÇÃO**

Ao calcular a folha de dissídio para um colaborador desligado em 15/03/2025, o sistema exibiu a mensagem de erro informando a ausência de convenção coletiva com cálculo de dissídio pendente para a referência selecionada.

**SOLUÇÃO**

**(1)** Acesse a tela **“Reajuste Salarial”** (Pessoal+ » Rotinas Folha » Reajuste Salarial) e marque as opções específicas para contemplar colaboradores desligados:

- **“Aplicar reajuste para demitidos entre a data-base e a assinatura”**
- **“Considerar projeção do aviso prévio indenizado dentro do mês da data-base”**

**(2)** Após aplicar o reajuste, acesse a tela **“Dissídio”** (Pessoal+ » Rotinas Folha » Cálculos » Dissídio) e realize o cálculo da folha de dissídio para o colaborador.

**(3)** Revise as configurações na tela **“Regras de Cálculo”** (Pessoal+ » Cadastros » Regras de Cálculo) e verifique se as opções estão de acordo com a política da empresa:

- **“Reajuste Sindical Proporcional ao Tempo de Serviço”**
- **“Considerar mês de admissão, independente dos dias trabalhados”**
- **“Aplicar percentual em todos os eventos da folha complementar (mensalistas)”**
- **“Considerar percentual cheio no recálculo de eventos”**

**Importante:** Mantenha a opção **“Considerar percentual cheio no recálculo de eventos”** desmarcada caso a empresa opte por aplicar o reajuste de forma proporcional aos eventos.

**CAUSA**

O reajuste salarial não foi aplicado ao colaborador desligado, impossibilitando o cálculo da folha de dissídio para a referência informada.
