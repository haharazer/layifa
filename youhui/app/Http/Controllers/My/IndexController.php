<?php
/**
 * Created by PhpStorm.
 * User: MyPC
 * Date: 2015/8/22
 * Time: 10:29
 */

namespace App\Http\Controllers;

class IndexController extends Controller
{
    public static function index($page = 1)
    {
        $pageSize = 12;
        $offset = ($page - 1) * $pageSize;
        $items = DB::table('discounts')->skip($offset)->take($pageSize)->orderBy('created_at', 'desc')-> get();

        return view('home', ['title' => '主页', 'items'=> $items, 'page' => $page]);
    }
} 