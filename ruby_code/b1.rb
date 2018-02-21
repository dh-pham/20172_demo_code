# puts "Hello word1!"
# names = [ "Suzuki" , "Kato" , "Tanaka" ]
# puts "#{names[0]}"

olympics = [
{year: 1896, city: "アテネ "} ,
{year: 1900, city: "パリ"} ,
{year: 1904, city: "センルイス ",note: "アメ リ カ初開催"} ,
{year: 1908, city: " ロ ン ド ン " } ,
{year: 1912, city: " ス ト ッ ク ホ ル ム "} ,
{year: 1916, city: " ベ ル リ ン ", note: "第 一 次 世 界 大戦で中止"} ,
{year: 1920, city: " ア ン ト ワ ープ "} ,
{year: 1924, city: " パ リ ", note: "同 じ 都 市 で の 2 回 目 の開催は初"} ,
{year: 1928, city: " アム ス テル ダム "} ,
{year: 1932, city: " ロ サ ン ゼ ルス "}
]


olympics.each do |olympic|
    puts "#{olympic[:year]} #{olympic[:city]}"
    if olympic[:note] != nil 
        puts "#{olympic[:note]}"
    end
end