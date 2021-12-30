class Build_Git:
    def __init__(self, system, branch, exp_interval):
        self.__system = system
        self.__branch = branch
        self.__exp_interval = exp_interval
        self.__changed_files = ''


    def pull(self): return self.__system.run(['git', 'pull'], self.__system.build_path)


    def get_changed_files(self):
        last_update = ['git',
                       'log',
                       self.__branch,
                       f'--since={self.__exp_interval}',
                       '--name-only',
                       f'--line-prefix={self.__system.build_path}' 
                       ]
        out = self.__system.run(last_update, self.__system.build_path)

        self.__changed_files = ''

        for x in out:
            if '.prw' in x.lower() and x not in self.__changed_files:
                self.__changed_files += ',' if self.__changed_files.__len__() > 0 else ''
                self.__changed_files += x

        return self.__changed_files