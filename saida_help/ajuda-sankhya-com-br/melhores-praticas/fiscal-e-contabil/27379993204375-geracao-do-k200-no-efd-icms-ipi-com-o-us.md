---
id: "27379993204375"
titulo: "Geração do K200 no EFD ICMS/IPI com o uso de notas Futuras"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27379993204375-Gera%C3%A7%C3%A3o-do-K200-no-EFD-ICMS-IPI-com-o-uso-de-notas-Futuras"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:39:40Z"
rotulos: ["Configuração", "NF-e", "IPI", "ICMS", "EFD", "Estoque", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Geração do K200 no EFD ICMS/IPI com o uso de notas Futuras"]
---

# Geração do K200 no EFD ICMS/IPI com o uso de notas Futuras

Quando a empresa opera com notas de vendas referentes a entregas futuras, é imprescindível que o parâmetro **"GERAK200CTE"** esteja **ativado**.

Caso este parâmetro esteja **desativado**, o sistema não realiza a validação, no momento da geração do SPED, das notas futuras no que diz respeito ao **estoque**, o que pode ocasionar divergências nos saldos.

Ao manter este parâmetro **ativado**, um novo campo será disponibilizado na geração do EFD ICMS/IPI:

![Imagem 1: Ao manter este parâmetro ativado , um novo campo será disponibilizado na geração do EFD ICMS/IPI:](https://ajuda.sankhya.com.br/hc/article_attachments/27543154412055)

- Na data do K200, deve ser informada a **última data** do mês ao qual se refere a entrega;
- Considerando que o arquivo foi entregue com saldo incorreto, uma vez que as notas com datas futuras não foram consideradas no estoque, recomenda-se consultar o departamento contábil para definir o procedimento adequado para a retificação.
