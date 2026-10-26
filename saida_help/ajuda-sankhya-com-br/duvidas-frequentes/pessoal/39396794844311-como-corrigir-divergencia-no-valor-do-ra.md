---
id: "39396794844311"
titulo: "Como corrigir divergência no valor do RAT após envio ao eSocial?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39396794844311-Como-corrigir-diverg%C3%AAncia-no-valor-do-RAT-ap%C3%B3s-envio-ao-eSocial"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-08-27T18:21:14Z"
rotulos: ["Configuração", "FAP", "Fiscal", "Impostos", "eSocial", "RAT", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Como corrigir divergência no valor do RAT após envio ao eSocial?

A divergência no valor do **"RAT"** (Riscos Ambientais do Trabalho) entre o sistema e o eSocial é uma situação comum que ocorre quando há inconsistência entre as configurações cadastradas no **"Registro Fiscal"** (Pessoal+ >> Cadastros >> Registro Fiscal) da empresa e os valores efetivamente enviados ao portal do eSocial. Esta discrepância impacta diretamente o cálculo da folha de pagamento, o resumo da GPS e a DCTFWeb.

O **"RAT"** é uma contribuição previdenciária calculada sobre a folha de salários, cuja alíquota varia conforme o grau de risco da atividade econômica da empresa. Quando multiplicado pelo **"FAP"** (Fator Acidentário de Prevenção), resulta no **"RAT Ajustado"**, que é o percentual efetivamente aplicado sobre a base de cálculo do INSS.

### Identificação da divergência

A divergência no **"RAT"** pode ser identificada ao comparar os valores apresentados no **"Resumo da Folha de Pagamento"** com os valores apurados no **"Resumo GPS do eSocial"**. Geralmente, o problema se manifesta quando:

- O percentual do **"RAT"** exibido no resumo GPS do eSocial difere do cadastrado no sistema.
- Os valores de contribuição previdenciária patronal apresentam diferenças entre o sistema e o eSocial.
- O campo **"Percentual Taxa de Seguro"** no **"Registro Fiscal"** está zerado ou com valor incorreto.
- O **"FAP"** não está preenchido ou está com valor fora da faixa permitida.

### Correção do RAT no cadastro da empresa

Para corrigir a divergência, ajuste as configurações no cadastro fiscal da empresa. Siga os passos abaixo:

**(1)** Acesse a tela **"Registro Fiscal"** (Pessoal+ >> Cadastros >> Registro Fiscal).

**(2)** Localize e selecione o registro fiscal que apresenta a divergência.

**(3)** Preencha corretamente o campo **"Taxa de Seguro (RAT)"** conforme o grau de risco da atividade.

**(4)** Preencha o campo **"Fator Acidentário de Prevenção (FAP)"** com o valor fornecido pelo órgão governamental, observando:
   • O valor deve conter exatamente 4 casas decimais (exemplo: 0,5000 ou 1,2502);

**(5)** Salve as alterações realizadas no cadastro.

![Imagem 1: (4) Preencha o campo "Fator Acidentário de Prevenção (FAP)" com o valor fornecido pelo órgão governamental, observando:…](https://ajuda.sankhya.com.br/hc/article_attachments/40798562898839)

**Atenção:** Após os ajustes no Registro Fiscal, realize a geração dos eventos S-1005 e S-1020 para validar se haverá necessidade de transmitir alterações ao eSocial.

### Validação dos valores corrigidos

Após realizar os ajustes valide se a correção foi efetiva:

**(1)** Gere o **"Resumo da Folha"** (Pessoal+ >> Rotinas Folha >> Gerenciador de Folhas) e verifique o campo **"RAT Ajustado FAP"**.

**(2)** Confirme se a alíquota apresentada corresponde ao cálculo: **"RAT"** × **"FAP"**.

**(3)** Verifique se o valor calculado está correto: (Base INSS - Licença Gestante) × **"RAT Ajustado"**.

**(4)** Compare os valores do **"Resumo GPS do eSocial"** com o **"Resumo da Folha"** para confirmar que não há mais divergências.

### Observações importantes

• Consulte sempre seu contador para obter os valores corretos de **"RAT"** e **"FAP"** para sua empresa.
• O **"FAP"** é divulgado anualmente pelo governo federal com base no histórico de acidentes de trabalho.
• Valores incorretos podem gerar rejeições no eSocial e divergências na DCTFWeb.
• Se houver processo administrativo ou judicial questionando o **"FAP"**, preencha também o grupo **"Processos relativos à Alíquota RAT"** no **"Registro Fiscal"**.
