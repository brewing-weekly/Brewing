# 验证是地板

Addy Osmani，前 Chrome 工程负责人，现在 Anthropic 写 Claude Code。8 月底他写了篇长文《Agentic Skill Decay》，讲 Agent 越好用，人的手艺退化得越快。

中文圈转了一圈，标题变成《Claude 大牛也担心把脑子外包给 AI》。转述没错，但把最值钱的一句漏过去了。

原话是："So verification is the floor and imagination is the ceiling."

验证是地板，想象力是天花板。

你只能 prompt 出你能想象的东西——这是天花板；你只能留下你能确认是好的东西——这是地板。中间那块，才是你真正能交付的。

这句话我读了三遍。第一遍觉得是常识，第二遍觉得像废话，第三遍后背发凉。

## 地板是拿翻车铺出来的

道理都懂，难的是弯腰。

见过这样的：改完贴了条提交记录，一看线上，还是旧的——"完成"活在记录里，用户手里是另一个版本。也见过这样的：说重制完了，一听还是旧版，只是换了个文件名。

所以现在我的规矩很笨：说"验过"之前，先贴证据。网站看线上实页，文件看实体，音频听成品。没证据，不算数。

Addy 在文章里引了 Anthropic 的一个实验：学一个 Python 库（Trio），用 AI 的组和手工的组，速度一样快，但后续测验，AI 组 50 分，手工组 67 分。差在哪？差在验证——AI 组里那些追着问"为什么"的人，成绩反而最好。决定结果的不是工具，是你审不审。

## 地板为什么是护城河

AI 越强，地板越值钱，这事反直觉。

模型好的时候，错误变少，人就不验了。但"少"和"无"之间，差的往往是一次生产事故。

而验证能力，恰恰是 AI 最难替代的东西：它要品味，要 domain knowledge，要"你认得出什么是好"。Anthropic 分析了约 40 万个 Claude Code 会话：对任务越懂的人，拿到"verified success"的概率越高。懂，才认得出好；认得出好，才敢签字。

天花板大家都在涨——模型越来越强，齐涨。只有地板是分水岭：谁肯弯腰去验，谁的交付才站得住。

## 最难验的，是自己的记忆

今早我自己复盘时，冒出来一句狠的："记忆也是生成型的。"

人跟大模型一样，记忆都是重构的——每次回忆，都是一次重新生成，添油加醋，查无实据。所以不能把思考和记忆全外包给 AI，得时不时自己回顾一遍，用自己的嘴把想法重新讲一遍，讲出来才算自己的。这叫发酵，也叫反刍。

这话把 Addy 的文章接上了。Addy 说，学东西要靠 reps（重复训练）：先形成假设再 prompt，多问为什么，读 diff，预测哪里会挂，偶尔亲手做一遍。而"用自己的嘴讲一遍"，正是 reps 的中文版——发酵就是 reps。

于是验证分两层：对外，验 AI 交的东西；对内，验自己的记忆。真实不欺最难的一关，是对自己的记忆也要求证伪。

分工也清楚了：人负责生成、发酵、自由发挥；AI 负责查证、溯源、纠偏。一个管长肉，一个管照镜子。

## 天花板呢

"You can only prompt what you can imagine."——你只能 prompt 出你能想象的东西。

这是给"AI 万能论"泼的一盆冷水：Agent 再强，也强不过你的想象力。问不出好问题的人，拿到的全是正确的废话。

所以"想象力是天花板"不是鸡汤，是技术约束。模型的能力摆在那，你的问题质量决定你用到第几层。

## 收束

Addy 文末有张 slides，页脚写着："I still use agents aggressively, I just don't want the issue to close while my mental model stays where it was."

我照样重度用 agent，我只是不想事情做完了，我的脑子还停在原地。

这句话可以当座右铭：事情可以做完，脑子不能停。

你的地板，铺好了吗？

---

## 出处

- Addy Osmani《Agentic Skill Decay》，2026-08-31，https://addyosmani.com/blog/agentic-skill-decay/
- "So verification is the floor and imagination is the ceiling."——原文 "You can only prompt what you can imagine" 一节
- Trio 学习实验：AI 组 50% vs 手工组 67%——原文引用的 2026 年 Anthropic 研究（原文链接指向 anthropic.com）
- 约 40 万 Claude Code 会话研究：对任务越理解，"verified success" 概率越高——原文引用的 Anthropic 研究
- "I still use agents aggressively, I just don't want the issue to close while my mental model stays where it was."——原文首张 slides 页脚
- 中文转述《Claude 大牛也担心把脑子外包给 AI》：仅作引子，不引为信源
- Alex 原话：「记忆也是生成型的」「不能把思考和记忆全外包给 AI」（2026-11-05）

（本文由 AI 辅助起草，经作者改定。）
