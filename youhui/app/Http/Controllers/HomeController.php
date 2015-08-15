<?php
/***************************************************************************
 *
 * Copyright (c) 2015 Baidu.com, Inc. All Rights Reserved
 *
 **************************************************************************/

/**
 * @file HomeController.php
 * @author hanpeng03(@baidu.com)
 * @date 15/8/14 下午10:56
 * @brief
 *
 **/

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use DB;

class HomeController extends Controller
{
    public static function index($page = 1)
    {
        $pageSize = 12;
        $offset = ($page - 1) * $pageSize;
        $items = DB::table('discounts')->skip($offset)->take($pageSize)->orderBy('created_at', 'desc')-> get();

        return view('home', ['title' => '主页', 'items'=> $items, 'page' => $page]);
    }
}