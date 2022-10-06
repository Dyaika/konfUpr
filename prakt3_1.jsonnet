local arr = std.range(1, 24);
local group(x) ="ИКБО-"+x+"-21";
local stud(age_, group_, name_) = {
    age: age_, group: group_, name: name_
};
{
groups:[
group(x)
for x in arr
],
students:[
stud(19,group(4),"Иванов И.И."),
stud(18,group(5),"Петров П.П."),
stud(18,group(5),"Сидоров С.С."),
stud(19,group(3),"Разшильдяев А.М."),
],
subject: "Конфигурационное управление"
}
