# -*- coding: UTF-8 -*-
# !/usr/bin/env python
'''

author: MRN6

updated: Jul. 18th, 2020 Sat. 03:40PM

LICENSE: CC0

'''

import re

class QPath:
    
    def __init__(self):
        pass
        
    def minimalpair(self, tag, html, position):
        #最小对称法
        check_start_tag='<'+tag
        check_end_tag=''
        if tag=='meta':
            check_end_tag='>'
        else:
            check_end_tag='</'+tag+'>'    
        start_tag_length=len(check_start_tag)
        end_tag_length=len(check_end_tag)
        length=len(html)
        index=position
        start=html.find(check_start_tag, index)
        if start>=0:
            require=1
        while require>0 and (index<length-1-start_tag_length and index<length-1-end_tag_length) :
            index=index+1
            if html[index:index+start_tag_length]==check_start_tag:
                require=require+1
            if html[index:index+end_tag_length]==check_end_tag:
                require=require-1
        return html[position:index+end_tag_length]
    
    def match(self, path=None, html=None):
        if path is None or html is None or len(path.strip())<=0 or len(html.strip())<=0:
            return []
        if not '//' in path:
            return []
        rules=path.split('//')
        matches=[]
        submatches=[]
        l=len(rules)
        c=0
        match_html=html
        for rule in rules:
            c=c+1
            if len(rule.strip())<1:
                continue
            if submatches is not None and len(submatches)>0:
                t=submatches
                submatches=[]
                for submatch in t:
                    if len(submatch.strip())<=0:
                        continue
                    attributecontent=''
                    if ':' in rule:
                        ruledatas=rule.split(':')
                        tag=ruledatas[0]
                        attributedatas=ruledatas[1].split('=')
                        attribute=attributedatas[0]
                        value=attributedatas[1]
                        attributecontent=attribute+'="'+value+'[^"]*"'
                    else:
                        tag=rule
                    tempmatches=re.findall('<'+tag+'[^<>]*'+attributecontent, submatch)
                    if tempmatches is None or tempmatches==[]:
                        continue
                    index=0
                    #print('[match-end]', tempmatches, '[/match-end]')
                    for tempmatch in tempmatches:
                        position=submatch.find(tempmatch, index)
                        while position>=0 and index<len(submatch):
                            match=self.minimalpair(tag, submatch, position)
                            index=position+len(match)
                            if c==l:
                                matches.append(match)
                            else:
                                submatches.append(match)
                            position=submatch.find(tempmatch, index)
            else:
                attributecontent=''
                attribute=None
                value=None
                if ':' in rule:
                    ruledatas=rule.split(':')
                    tag=ruledatas[0]
                    attributedatas=ruledatas[1].split('=')
                    attribute=attributedatas[0]
                    value=attributedatas[1]
                    attributecontent=attribute+'="'+value+'[^"]*"'
                else:
                    tag=rule
                tempmatches=re.findall('<'+tag+'[^<>]*'+attributecontent, match_html)
                if tempmatches is None or tempmatches==[]:
                    return []
                index=0
                #print('[match-root]', tempmatches, '[/match-root]')
                for tempmatch in tempmatches:
                    if not tag in tempmatch or (attribute is not None and value is not None and not attribute+'="'+value+'"' in tempmatch):
                        continue
                    position=match_html.find(tempmatch, index)
                    while position>=0 and index<len(html)-1:
                        match=self.minimalpair(tag, match_html, position)
                        #print(position, '[match-sub]', match, '[/match-sub]')
                        index=position+len(match)
                        if c==l:
                            matches.append(match)
                        else:
                            submatches.append(match)
                        position=match_html.find(tempmatch, index)
        return matches
    
qpath=QPath()