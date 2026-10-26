---
id: "26611459117079"
titulo: "EFD FISCAL ICMS/IPI - Registro C170 - Campo 20 CST_IPI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26611459117079-EFD-FISCAL-ICMS-IPI-Registro-C170-Campo-20-CST-IPI"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:41:06Z"
rotulos: ["Configuração", "NF-e", "IPI", "ICMS", "Impostos", "EFD", "Registro C170 - Campo 20 CST_IPI", "Considerar NF-e Cancelada Extemporânea como Cancelada no mês no EFD"]
---

# EFD FISCAL ICMS/IPI - Registro C170 - Campo 20 CST_IPI

Ao gerar o EFD Fiscal, é possível se deparar com um problema no qual o campo **"20 CST\_IPI"** não está sendo preenchido, conforme está na nota fiscal. Para resolver essa questão, analise a seguinte configuração, nas preferências da empresa (comercial):

![Imagem 1: Ao gerar o EFD Fiscal, é possível se deparar com um problema no qual o campo "20 CST_IPI" não está sendo preenchido,…](https://ajuda.sankhya.com.br/hc/article_attachments/26667101767703)

Se o campo **"Considerar NF-e Cancelada Extemporânea como Cancelada no mês no EFD"** estiver como **"OUTROS",** mesmo havendo CST de IPI informado na nota fiscal, o sistema não o levará para o registro C170 no campo 20.
