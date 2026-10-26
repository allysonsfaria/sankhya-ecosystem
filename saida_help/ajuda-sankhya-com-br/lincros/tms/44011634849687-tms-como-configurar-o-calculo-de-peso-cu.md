---
id: "44011634849687"
titulo: "[TMS] Como configurar o cálculo de peso “Cubagem”?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011634849687--TMS-Como-configurar-o-c%C3%A1lculo-de-peso-Cubagem"
trilha: "Lincros > TMS"
atualizado_em: "2026-10-05T19:07:55Z"
rotulos: ["sync_hc", "lincros", "lincros_13438059", "sync_hash_156271ce978a"]
---

# [TMS] Como configurar o cálculo de peso “Cubagem”?

**Menu:** Cadastros Gerais > Transportadora > Transportadora Empresa > Cadastro

**Objetivo:** Apresentar a configuração utilizada no cadastro da Transportadora Empresa, para que o sistema TMS, realize a leitura correta da cubagem.

**Considerações:** Temos situações em que o Frete Valor é definido conforme o maior valor do “Frete Peso”, para isso o sistema compara o maior valor entre “Peso Nominal” e “Peso Cubado”.

Mesmo com este componente devidamente cadastrado na tabela, ocorrem divergências no valor do frete calculado, porque ocorre esse comportamento?

Para que o sistema possa calcular corretamente a cubagem, utilizada pela transportadora, precisamos inserir no cadastro “Transportadora Empresa” a “Expressão leitura cubagem”.

![Imagem 1: Para que o sistema possa calcular corretamente a cubagem, utilizada pela transportadora, precisamos inserir no cadastro…](https://ajuda.sankhya.com.br/hc/article_attachments/44011619954839)

Como neste exemplo(//\*/infCarga/infQ[tpMed='CUBAGEM BASE CALCULO']/qCarga)

Além deste cadastro, é necessário marcar a flag “Considerar cubagem do CT-e”.

![Imagem 2: Além deste cadastro, é necessário marcar a flag “Considerar cubagem do CT-e”.](https://ajuda.sankhya.com.br/hc/article_attachments/44011626985367)

**Conclusão:** Desta forma ao importar o CT-E, o sistema vai ler a tag correta do XML e aplicar o cálculo correto.
