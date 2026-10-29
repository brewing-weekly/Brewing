# 《酝酿》第 4 期：翻车变本能，信息流的判断力

> 一夕运粮，一期酝酿。

《酝酿》是一份产业与认知周刊，每周五从本周的收藏里酿出十条。

## 本期主判断

**翻车变本能不是 AI 的问题，是经验固化的方法问题。** 本期十条从「翻车怎么变能力」到「怎么识别被喂了噪声」，到「工具选到该停手了」。三件事合起来是同一件：用 AI 越多，留给人手里判断的成分越重。

## 工具与方法

1. [贩卖怀疑的商人：李翔拆解烟草业半世纪的「怀疑武器」](https://mp.weixin.qq.com/s/Vwvpb-43w1a5e2buN7JQiw)
   三步方法论：提供对抗性事实→营造不确定性→削弱核心事实，1969年烟草业备忘录原话"怀疑是最好的手段"。权威人物、媒体平衡、心理误区三个杠杆，可套进任何行业叙事审读。（来源：李翔，2026-10）

2. [斯坦福 CS146S：如何打造 always-on agent](https://mp.weixin.qq.com/s/gz8ZjplJ40agZKsgbFAXSA)
   能力阶梯、动态工具发现、上下文工程=harness工程、提示缓存、记忆四层、飞轮预训练→SFT→RL。核心：主agent保持稀疏，重活交子agent用完即弃；没有缓存命中即bug。（来源：深思圈，讲者Lee Robinson，2026-10）

3. [An Illustrated Guide to AI Agents 书介：450页图解](https://mp.weixin.qq.com/s/vrQTIvpI1caVMT8JRzEi5Q)
   不把Agent当黑箱：状态+工具+规划+检查四层；记忆四类（工作/情景/语义/程序）对应工程实现；评估章点破Agent评估难点——行为多步、依赖上下文，没有干净准确率指标。（来源：Eva抓取，2026-10）

4. [Tailscale SSH 漏洞：一台失守，多台沦陷](https://mp.weixin.qq.com/s/rA97NXCBX9aAC3gsdTwL7w)
   11项安全问题，最严重：攻击者控制一台设备后可利用Tailscale SSH获得其他服务器root权限，自动传播每攻陷一台不到1秒（测试版本：v1.104.2/headscale v0.29.5）。官方修复中，建议暂时关闭Tailscale SSH或收紧访问权限。（来源：公众号，2026-10）

5. [全木典籍：翻译理论四家——鲁迅、林语堂、傅雷、钱钟书](https://mp.weixin.qq.com/s/lKAdvdJvLTJO3ixW1Z_-gg)
   鲁迅「宁信而不顺」、林语堂「忠实通顺美」、傅雷「神似」、钱钟书「达为信之前提」，四位对信达雅的回应与分歧。傅雷「神似」最贴近AI翻译的判断边界：形似容易，神似要人工把关。（来源：全木典籍，4,859字，2026-10）

## 书与思考

1. [点拾投资：《谁在制造世界？》——全价值链出海](https://mp.weixin.qq.com/s/0h_Wr8uu0SIZyLmxjWVweQ)
   三例论证：卫生纸绕半个地球的北欧/南美分工、iPhone零部件旅程25万公里（绕地球六圈多）、A350机翼机身尾翼三国总装——"全价值链出海"不是产能出口，是看懂全球深层依赖网络。（来源：点拾投资，2026-10）

2. [点拾投资：《造神之后》——AI对齐的终极考验](https://mp.weixin.qq.com/s/BtlheHZVVIlg1frLoWaJ0A)
   Robert Wright（《非人类》作者）新作，中文版2026-10湛庐文化出版。核心反讽：AI不需要野心也会完成任务中寻求权力（回形针最大化）；危险不在AI恨我们，在它太听话想把事做完；对齐AI终会变成人类自己跟自己对齐。（来源：点拾投资，2026-10）

3. [《像统计学家一样思考》——Bradley Efron的认知装备清单](https://mp.weixin.qq.com/s/6cvh6CvaN3lHvPlnZLYk_A)
   87岁统计学家（自助法发明者）写的认知侦探案合集：均值回归、等待悖论、Fisher随机化，三个生存问题：数据有资格进入吗？噪声之下有东西吗？我凭什么相信？（来源：羽飞扬书评，2026-10）

4. [《Good Writing：写好一个英文句子》——36条规则，重点看前12条](https://mp.weixin.qq.com/s/HmFYSn0DGbTFttrJMehWsQ)
   Anne Lamott等编著，先写好一个句子再管段落；删掉very再看（crutch word）；"Easy reading is damn hard writing"；表达声音比技巧重要。写代码注释、写文档，同一套。（来源：公众号，2026-10）

## 工具推荐

1. [BookOrbit：自托管家庭阅读平台（5,428 Star）](https://github.com/bookorbit/bookorbit)
   EPUB/PDF/漫画/有声书统一管理；Docker Compose+PostgreSQL+本地文件；iPhone（iOS 26+）/Apple Watch（watchOS 26+）/Kobo/KOReader；阅读统计含年度目标热力图。（来源：搭把手科技《GitHub 每日一荐 074》，2026-10）

---

一夕运粮，一期酝酿。zhangxunnj · 2026-11-02
